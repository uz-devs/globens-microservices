from psycopg2 import extras as psycopg2_extras
from datetime import datetime
from tools import settings
from tools import utils
import psycopg2


# region commons
def get_db_connection():
    reconnect = settings.db_conn is None

    if not reconnect:
        try:
            settings.db_conn.cursor().execute('select 1;')
        except psycopg2.OperationalError:
            reconnect = True

    if reconnect:
        settings.db_conn = psycopg2.connect(
            host=settings.db_settings['host'],
            database=settings.db_settings['database'],
            user=settings.db_settings['user'],
            password=settings.db_settings['password']
        )
        print('database (re)initialized', settings.db_conn)

    return settings.db_conn


def end():
    get_db_connection().close()


# endregion


# region user management
def get_user(email=None, user_id=None, session_key=None):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    if email is not None:
        cur.execute('select * from "gb_user" where "email" = %s;', (
            email,
        ))
    elif user_id is not None:
        cur.execute('select * from "gb_user" where "id" = %s;', (
            user_id,
        ))
    elif session_key is not None:
        cur.execute('select * from "gb_user" where "sessionKey" = %s;', (
            session_key,
        ))
    gb_user = cur.fetchone()
    cur.close()
    return gb_user


def create_user(email, name, picture, token, auth_mode):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    session_key = utils.md5(value=f'{email}{utils.now_us()}')
    cur.execute('insert into "gb_user"("email", "name", "picture","pictureBlob","tokens","sessionKey","authMode") values (%s,%s,%s,%s,%s,%s,%s);', (
        email,
        name,
        picture,
        utils.load_picture_bytes(picture=picture),
        token,
        session_key,
        auth_mode
    ))

    cur.close()
    get_db_connection().commit()
    return get_user(email=email), session_key


def update_user(gb_user, country_code=None, google_drive_email=None):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    sql_set_cols, sql_set_values = [], ()
    if country_code:
        sql_set_cols += ['countryCode']
        sql_set_values += (country_code,)
    if google_drive_email:
        sql_set_cols += ['googleDriveEmail']
        sql_set_values += (google_drive_email,)

    if len(sql_set_cols) + len(sql_set_values) > 0:
        cur.execute(f'update "gb_user" set {", ".join([f"{col} = %s" for col in sql_set_cols])} where "id"=%s;', sql_set_values + (gb_user['id'],))
        cur.close()
        get_db_connection().commit()


# endregion


# region business page management
def get_business_page_ids(gb_user):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    # step 1 : get user's jobs (from vacancies table)
    cur.execute('select * from "gb_job" where "user_id"=%s;', (
        gb_user['id'],
    ))
    gb_job = cur.fetchall()

    # step 2 : get unique campaigns related of the jobs/vacancies
    business_page_ids = set()
    for gb_job in gb_job:
        cur.execute('select "id" from "gb_business_page" where "id" = %s;', (
            gb_job['business_page_id'],
        ))
        business_page_ids.add(cur.fetchone()[0])

    cur.close()
    return list(business_page_ids)


def get_business_page(business_page_id):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select * from "gb_business_page" where "id" = %s;', (
        business_page_id,
    ))
    gb_business_page = cur.fetchone()

    cur.close()
    return gb_business_page


def get_user_role_in_business_page(gb_user, gb_business_page):
    cur = get_db_connection().cursor()

    cur.execute('select "role" from "gb_job" where "user_id" = %s and "business_page_id" = %s;', (
        gb_user['id'],
        gb_business_page['id'],
    ))
    gb_job = cur.fetchone()

    cur.close()
    return "consumer" if gb_job is None else gb_job[0]


def create_business_page(gb_user, title, picture_blob, country_code):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    # create a large business page
    cur.execute('insert into "gb_business_page"("title", "type", "pictureBlob", "countryCode") values (%s,%s,%s,%s) returning "id";', (
        title,
        'large business',
        psycopg2.Binary(picture_blob),
        country_code
    ))
    business_page_id = cur.fetchone()[0]

    # create business owner job position for the business page
    cur.execute('insert into gb_job("title", "role", "business_page_id") values (%s,%s,%s) returning "id";', (
        'Business owner',
        'business owner',
        business_page_id
    ))
    business_owner_job_id = cur.fetchone()[0]

    # map the user with the business owner vacancy (empty job position)
    cur.execute('update gb_job set "user_id" = %s where "id" = %s;', (
        gb_user['id'],
        business_owner_job_id
    ))

    cur.close()
    get_db_connection().commit()


def get_business_page_job_ids(gb_business_page):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select "id" from "gb_job" where "business_page_id" = %s;', (
        gb_business_page['id'],
    ))
    job_ids = [job_id[0] for job_id in cur.fetchall()]

    cur.close()
    return job_ids


def update_business_page_details(gb_business_page, title, picture_blob, country_code):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('update "gb_business_page" set "title" = %s, "pictureBlob" = %s, "countryCode" = %s where "id"=%s;', (
        title,
        picture_blob,
        country_code,
        gb_business_page['id']
    ))

    cur.close()
    get_db_connection().commit()


# endregion


# region product management
def create_product(gb_user, gb_business_page, gb_category, name, product_type, picture_blob, price, currency, description, contents, dynamic_link):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('insert into "gb_product"("name", "productType", "pictureBlob", "price", "currency", "description", "contents", "dynamicLink", "business_page_id", "category_id") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) returning "id";', (
        name,
        product_type,
        picture_blob,
        price,
        currency,
        description,
        contents,
        dynamic_link,
        gb_business_page['id'],
        gb_category['id'],
    ))
    new_product_id = cur.fetchone()[0]

    cur.execute('insert into "gb_product_log"("timestamp", "action", "product_id", "user_id") values (%s,%s,%s,%s);', (
        datetime.now(),
        'create',
        new_product_id,
        gb_user['id']
    ))

    cur.close()
    get_db_connection().commit()
    return new_product_id


def update_product(gb_product, gb_business_page, gb_category, name, product_type, picture_blob, price, currency, description, contents, dynamic_link):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('update "gb_product" set "name" = %s, "productType" = %s, "pictureBlob" = %s, "business_page_id" = %s, "category_id" = %s, "price" = %s, "currency" = %s, "description" = %s, "contents" = %s, "dynamicLink" = %s where "id"=%s;', (
        name,
        product_type,
        picture_blob,
        gb_business_page['id'],
        gb_category['id'],
        price,
        currency,
        description,
        contents,
        dynamic_link,
        gb_product['id']
    ))

    cur.close()
    get_db_connection().commit()


def create_product_publish_request(gb_product, gb_product_business_page, gb_requester_user):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('insert into "gb_product_publish_request"("timestamp", "countryCode", "product_id", "business_page_id", "requester_user_id") values(%s,%s,%s,%s,%s);', (
        datetime.now(),
        gb_product_business_page['countryCode'],
        gb_product['id'],
        gb_product_business_page['id'],
        gb_requester_user['id']
    ))
    cur.close()
    get_db_connection().commit()


def get_product_publish_request(gb_product):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "gb_product_publish_request" where "product_id"=%s;', (gb_product['id'],))
    gb_request = cur.fetchone()
    cur.close()
    return gb_request


def unpublish_product(gb_product):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('update "gb_product" set "published" = %s where "id"=%s;', (
        False,
        gb_product['id']
    ))

    cur.close()
    get_db_connection().commit()


def create_content(title, file_id, url):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('insert into "gb_content"("title", "fileId", "url") values (%s,%s,%s) returning "id";', (
        title,
        file_id,
        url,
    ))
    new_content_id = cur.fetchone()[0]

    cur.close()
    get_db_connection().commit()
    return new_content_id


def get_content(content_id):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select * from "gb_content" where "id"=%s;', (content_id,))
    gb_content = cur.fetchone()

    cur.close()
    return gb_content


def update_content(gb_content, title, file_id, url):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('update "gb_content" set "title" = %s, "fileId" = %s, "url" = %s where "id"=%s;', (
        title,
        file_id,
        url,
        gb_content['id'],
    ))

    cur.close()
    get_db_connection().commit()


def delete_content(gb_content):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('delete from "gb_content" where "id"=%s;', (gb_content['id'],))
    cur.close()
    get_db_connection().commit()


def get_next_k_products(previous_product_id, k, filter_details):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    sql_filter_map = {}
    if filter_details.useFilter:
        # (1) filter mode
        if previous_product_id > -1:
            sql_filter_map['"id" >= %s'] = previous_product_id
        if filter_details.categoryId > -1:
            sql_filter_map['"category_id" = %s'] = filter_details.categoryId
        if filter_details.publishedProductsOnly is True:
            sql_filter_map['published = %s'] = True
        if filter_details.substring:
            sql_filter_map['"name" like %s'] = filter_details.substring
        if filter_details.regex:
            sql_filter_map['"name" like %s'] = filter_details.regex
        if filter_details.businessPageId > -1:
            sql_filter_map['"business_page_id" = %s'] = filter_details.businessPageId

    sql_command_args = tuple()
    sql_where_clause_str = ''
    if len(sql_filter_map) == 1:
        key = next(iter(sql_filter_map.keys()))
        sql_where_clause_str = f'where {key}'
        sql_command_args += (sql_filter_map[key],)
    elif len(sql_filter_map) > 1:
        keys = list(sql_filter_map.keys())
        sql_where_clause_str = f'where {" and ".join(keys)}'
        for key in keys:
            sql_command_args += (sql_filter_map[key],)
    sql_command_args += (k,)
    cur.execute(f'select * from "gb_product" {sql_where_clause_str} order by "id" limit %s;', sql_command_args)
    gb_products = cur.fetchall()

    cur.close()
    return [] if gb_products is None else gb_products


def get_product(product_id):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "gb_product" where "id" = %s;', (
        product_id,
    ))
    gb_product = cur.fetchone()

    cur.close()
    return gb_product


def get_product_categories():
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "gb_product_category";')
    gb_products = cur.fetchall()
    cur.close()
    return gb_products


def get_product_category(category_id):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select * from "gb_product_category" where "id"=%s;', (category_id,))

    gb_product = cur.fetchone()
    cur.close()
    return gb_product


# endregion


# region job/vacancy management
def create_vacant_job(gb_user, gb_business_page, title):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('insert into "gb_job"("title", "role", "business_page_id") values (%s,%s,%s) returning "id";', (
        title,
        'employee',
        gb_business_page['id']
    ))
    new_job_id = cur.fetchone()[0]

    cur.execute('insert into "gb_job_log"("timestamp", "action", "job_id", "user_id") values (%s,%s,%s,%s);', (
        datetime.now(),
        'create',
        new_job_id,
        gb_user['id']
    ))

    cur.close()
    get_db_connection().commit()


def get_next_k_vacant_jobs(previous_vacant_job_id, k, filter_details):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    if filter_details.useFilter:
        if previous_vacant_job_id is None:
            cur.execute('select * from "gb_job" where "user_id" is null and "title" like %s order by "id" limit %s;', (
                f'%{filter_details.filterText}%',
                k
            ))
        else:
            cur.execute('select * from "gb_job" where "id" > %s and "user_id" is null and "title" like %s order by "id" limit %s;', (
                previous_vacant_job_id,
                f'%{filter_details.filterText}%',
                k
            ))
    else:
        if previous_vacant_job_id is None:
            cur.execute('select * from "gb_job" where "user_id" is null order by "id" limit %s;', (
                k
            ))
        else:
            cur.execute('select * from "gb_job" where "id" > %s and "user_id" is null order by "id" limit %s;', (
                previous_vacant_job_id,
                k
            ))
    gb_vacancies = cur.fetchall()

    cur.close()
    return [] if gb_vacancies is None else gb_vacancies


def get_job(job_id):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select * from "gb_job" where "id" = %s;', (
        job_id,
    ))
    gb_job = cur.fetchone()

    cur.close()
    return gb_job


# endregion


# region job/vacancy application management
def create_job_application(gb_user, gb_job, message, contents):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('insert into "gb_job_application"("message", "contents", "user_id", "job_id") values (%s,%s,%s,%s);', (
        message,
        contents,
        gb_user['id'],
        gb_job['id']
    ))

    cur.close()
    get_db_connection().commit()


def get_job_application_ids(gb_job):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select "id" from "gb_job_application" where "job_id" = %s;', (
        gb_job['id'],
    ))
    job_ids = [job_id[0] for job_id in cur.fetchall()]

    cur.close()
    return job_ids


def get_job_application(job_application_id=None, gb_user=None, gb_job=None):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    if job_application_id is not None:
        cur.execute('select * from "gb_job_application" where "id" = %s;', (
            job_application_id,
        ))
    elif None not in [gb_user, gb_job]:
        cur.execute('select * from "gb_job_application" where "user_id"=%s and "job_id"=%s;', (
            gb_user['id'],
            gb_job['id']
        ))

    gb_job = cur.fetchone()
    cur.close()
    return gb_job


def job_application_exists(gb_user, gb_job):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select exists(select * from "gb_job_application" where "user_id"=%s and "job_id"=%s);', (
        gb_user['id'],
        gb_job['id']
    ))
    exists = cur.fetchone()[0]

    cur.close()
    return exists


def approve_job_application(gb_job_application):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('update "gb_job" set "user_id" = %s where "id" = %s;', (
        gb_job_application['user_id'],
        gb_job_application['job_id']
    ))

    cur.close()
    get_db_connection().commit()


def decline_job_application(gb_job_application):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('delete from "gb_job_application" where "id"=%s;', (
        gb_job_application['id'],
    ))

    cur.close()
    get_db_connection().commit()


# endregion


# region review management
def create_or_update_product_review(gb_user, gb_product, stars, text, timestamp):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select exists(select * from "gb_product_review" where "user_id"=%s and "product_id"=%s);', (
        gb_user['id'],
        gb_product['id']
    ))
    exists = cur.fetchone()[0]
    if exists:
        cur.execute('delete from "gb_product_review" where "user_id" = %s and "product_id" = %s;', (
            gb_user['id'],
            gb_product['id']
        ))
    cur.execute('insert into "gb_product_review"("stars", "text", "timestamp", "user_id", "product_id") values (%s,%s,%s,%s,%s);', (
        stars,
        text,
        timestamp,
        gb_user['id'],
        gb_product['id']
    ))

    cur.close()
    get_db_connection().commit()


def get_product_reviews(gb_product):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "gb_product_review" where "product_id"=%s', (gb_product['id'],))
    rows = cur.fetchall()
    cur.close()
    return rows


def get_product_review(product_review_id):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "gb_product_review" where "id" = %s;', (product_review_id,))
    gb_product_review = cur.fetchone()
    cur.close()
    return gb_product_review


def delete_product_review(gb_product_review):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('delete from "gb_product_review" where "id"=%s;', (gb_product_review['id'],))
    cur.close()
    get_db_connection().commit()


def create_or_update_employee_review(gb_user, gb_business_page, gb_employee_user, text, timestamp):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)

    cur.execute('select exists(select * from "gb_employee_review" where "user_id"=%s and "business_page_id"=%s and "employee_id"=%s);', (
        gb_user['id'],
        gb_business_page['id'],
        gb_employee_user['id']
    ))
    exists = cur.fetchone()[0]

    if exists:
        cur.execute('update "gb_employee_review" set "text" = %s, "timestamp" = %s where "user_id" = %s and "business_page_id" = %s and "employee_id"=%s;', (
            text,
            timestamp,
            gb_user['id'],
            gb_business_page['id'],
            gb_employee_user['id']
        ))
    else:
        cur.execute('insert into "gb_employee_review"("text", "timestamp", "user_id", "business_page_id", "employee_id") values (%s,%s,%s,%s,%s);', (
            text,
            timestamp,
            gb_user['id'],
            gb_business_page['id'],
            gb_employee_user['id'],
        ))

    cur.close()
    get_db_connection().commit()


def get_employee_reviews(gb_business_page, gb_employee_user):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "gb_employee_review" where "business_page_id"=%s and "employee_id"=%s', (
        gb_business_page['id'],
        gb_employee_user['id']
    ))
    rows = cur.fetchall()
    cur.close()
    return rows


def get_employee_review(employee_review_id):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "gb_employee_review" where "id" = %s;', (employee_review_id,))
    gb_employee_review = cur.fetchone()
    cur.close()
    return gb_employee_review


def delete_employee_review(gb_employee_review):
    cur = get_db_connection().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('delete from "gb_employee_review" where "id"=%s;', (gb_employee_review['id'],))
    cur.close()
    get_db_connection().commit()

# endregion
