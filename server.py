# import the generated gRPCs
from gb_grpcs import gb_service_pb2_grpc
from gb_grpcs import gb_service_pb2
# others
from concurrent import futures
from tools import db_mgr as db
from tools import utils
import grpc
import time
import json


class GlobensServiceServicer(gb_service_pb2_grpc.GlobensServiceServicer):
    # region user management module
    def authenticateUser(self, request, context):
        print(f' authenticateUser')
        response = gb_service_pb2.AuthenticateUser.Response()
        response.success = False

        method = request.method
        tokens = json.loads(s=request.tokensJson)

        if method == gb_service_pb2.AuthenticateUser.AuthMethod.GOOGLE:
            user_profile = utils.load_google_profile(id_token=tokens['idToken'])
            gb_user, session_key = db.create_or_update_user(
                email=user_profile['email'],
                name=user_profile['name'],
                picture=user_profile['picture'],
                tokens=request.tokensJson
            )
            response.userId = gb_user['id']
            response.sessionKey = session_key
            response.success = True
        elif method == gb_service_pb2.AuthenticateUser.AuthMethod.FACEBOOK:
            user_profile = utils.load_facebook_profile(access_token=tokens['accessToken'])
            gb_user, session_key = db.create_or_update_user(
                email=user_profile['email'],
                name=user_profile['name'],
                picture=user_profile['picture'],
                tokens=request.tokensJson
            )
            response.userId = gb_user['id']
            response.sessionKey = session_key
            response.success = True
        elif method == gb_service_pb2.AuthenticateUser.AuthMethod.KAKAOTALK:
            print(tokens['accessToken'])
        elif method == gb_service_pb2.AuthenticateUser.AuthMethod.PHONE:
            print(tokens)
        elif method == gb_service_pb2.AuthenticateUser.AuthMethod.APPLE:
            print(tokens)

        print(f' authenticateUser, success={response.success}')
        return response

    def deactivateUser(self, request, context):
        print(f' deactivateUser')
        # todo deactivate user
        print(f' deactivateUser')

    def updateUserDetails(self, request, context):
        print(f' updateUserDetails')
        # todo update user details
        print(f' updateUserDetails')

    def fetchUserDetails(self, request, context):
        print(f' fetchUserDetails')
        response = gb_service_pb2.FetchUserDetails.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_target_user = db.get_user(user_id=request.userId)

        if None not in [gb_user, gb_target_user]:
            response.id = gb_target_user['id']
            response.email = gb_target_user['email']
            response.name = gb_target_user['name']
            response.picture = gb_target_user['picture']
            response.pictureBlob = bytes(gb_target_user['pictureBlob'])
            response.success = True

        print(f' fetchUserDetails, success={response.success}')
        return response

    # endregion

    # region job/vacancy management module
    def createVacantJob(self, request, context):
        print(f' createVacantJob')
        response = gb_service_pb2.CreateVacantJob.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_business_page = db.get_business_page(business_page_id=request.businessPageId)

        if None not in [gb_user, gb_business_page]:
            db.create_vacant_job(gb_user=gb_user, gb_business_page=gb_business_page, title=request.title)
            response.success = True

        print(f' createVacancy, success={response.success}')
        return response

    def updateJobDetails(self, request, context):
        print(f' updateJobDetails')
        # todo update job details
        print(f' updateJobDetails')

    def uncreateJob(self, request, context):
        print(f' uncreateJob')
        # todo uncreate job
        print(f' uncreateJob')

    def fetchBusinessPageJobIds(self, request, context):
        print(f' fetchBusinessPageJobIds')
        response = gb_service_pb2.FetchBusinessPageJobIds.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_business_page = db.get_business_page(business_page_id=request.businessPageId)

        if None not in [gb_user, gb_business_page]:
            response.id.extend(db.get_business_page_job_ids(gb_business_page=gb_business_page))
            response.success = True

        print(f' fetchBusinessPageJobIds, success={response.success}')
        return response

    def fetchNextKVacantJobIds(self, request, context):
        print(f' fetchNextKVacantJobIds')
        response = gb_service_pb2.FetchNextKVacantJobIds.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        k = request.k
        filter_details = request.filterDetails
        previous_vacant_job_id = request.previousVacantJobId

        if None not in [gb_user, k, filter_details] and k <= 250:
            for gb_vacant_job in db.get_next_k_vacant_jobs(previous_vacant_job_id=previous_vacant_job_id, k=k, filter_details=filter_details):
                response.id.extend([gb_vacant_job['id']])
            response.success = True

        print(f' fetchNextKVacancyJobIds, success={response.success}')
        return response

    def fetchJobDetails(self, request, context):
        print(f' fetchJobDetails')
        response = gb_service_pb2.FetchJobDetails.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_job = db.get_job(job_id=request.jobId)

        if None not in [gb_user, gb_job]:
            response.id = gb_job['id']
            response.role = gb_job['role']
            response.title = gb_job['title']
            response.hiredUserId = gb_job['user_id'] if gb_job['user_id'] is not None else -1
            response.success = True

        print(f' fetchJobDetails, success={response.success}')
        return response

    # endregion

    # region vacancy application management module
    def createJobApplication(self, request, context):
        print(f' createJobApplication')
        response = gb_service_pb2.CreateJobApplication.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_job = db.get_job(job_id=request.jobId)

        if None not in [gb_user, gb_job] and gb_job['user_id'] is None and not db.job_application_exists(gb_user=gb_user, gb_job=gb_job):
            db.create_job_application(gb_user=gb_user, gb_job=gb_job, message=request.message)
            response.success = True

        print(f' createJobApplication, success={response.success}')
        return response

    def updateJobApplicationDetails(self, request, context):
        print(f' updateJobApplicationDetails')
        # todo update vacancy application
        print(f' updateJobApplicationDetails')

    def uncreateJobApplication(self, request, context):
        print(f' uncreateJobApplication')
        # todo uncreate vacancy application
        print(f' uncreateJobApplication')

    def fetchJobApplicationIds(self, request, context):
        print(f' fetchJobApplicationIds')
        response = gb_service_pb2.FetchJobApplicationIds.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_job = db.get_job(job_id=request.jobId)

        if None not in [gb_user, gb_job]:
            response.id.extend(db.get_job_application_ids(gb_job=gb_job))
            response.success = True

        print(f' fetchJobApplicationIds, success={response.success}')
        return response

    def fetchJobApplicationDetails(self, request, context):
        print(f' fetchJobApplicationDetails')
        response = gb_service_pb2.FetchJobApplicationDetails.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_job_application = db.get_job_application(job_application_id=request.jobApplicationId)

        if None not in [gb_user, gb_job_application]:
            response.id = gb_job_application['id']
            response.message = gb_job_application['message']
            response.applicantId = gb_job_application['user_id']
            response.success = True

        print(f' fetchJobApplicationDetails, success={response.success}')
        return response

    def approveJobApplication(self, request, context):
        print(f' approveJobApplication')
        response = gb_service_pb2.ApproveJobApplication.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_job_application = db.get_job_application(job_application_id=request.jobApplicationId)

        if None not in [gb_user, gb_job_application]:
            db.approve_job_application(gb_job_application=gb_job_application)
            response.success = True

        print(f' approveJobApplication, success={response.success}')
        return response

    def declineJobApplication(self, request, context):
        print(f' declineJobApplication')
        response = gb_service_pb2.DeclineJobApplication.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_job_application = db.get_job_application(job_application_id=request.jobApplicationId)

        if None not in [gb_user, gb_job_application]:
            db.decline_job_application(gb_job_application=gb_job_application)
            response.success = True

        print(f' declineJobApplication, success={response.success}')
        return response

    # endregion

    # region business page management module
    def createBusinessPage(self, request, context):
        print(f' createBusinessPage')
        response = gb_service_pb2.CreateBusinessPage.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)

        if gb_user is not None:
            db.create_business_page(gb_user=gb_user, title=request.title, picture_blob=request.pictureBlob)
            response.success = True

        print(f' createBusinessPage, success={response.success}')
        return response

    def updateBusinessPageDetails(self, request, context):
        print(f' updateBusinessPageDetails')
        # todo update business page details
        print(f' updateBusinessPageDetails')

    def uncreateBusinessPage(self, request, context):
        print(f' uncreateBusinessPage')
        # todo uncreate business page
        print(f' uncreateBusinessPage')

    def fetchMyBusinessPageIds(self, request, context):
        print(f' fetchMyBusinessPageIds')
        response = gb_service_pb2.FetchMyBusinessPageIds.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)

        if gb_user is not None:
            response.id.extend(db.get_business_page_ids(gb_user=gb_user))
            response.success = True

        print(f' fetchMyBusinessPageIds, success={response.success}')
        return response

    def fetchBusinessPageDetails(self, request, context):
        print(f' fetchBusinessPageDetails')
        response = gb_service_pb2.FetchBusinessPageDetails.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_business_page = db.get_business_page(business_page_id=request.businessPageId)

        if None not in [gb_user, gb_business_page]:
            response.id = gb_business_page['id']
            response.title = gb_business_page['title']
            response.type = gb_business_page['type']
            response.pictureBlob = bytes(gb_business_page['pictureBlob'])
            response.role = db.get_user_role_in_business_page(gb_user=gb_user, gb_business_page=gb_business_page)
            response.success = True

        print(f' fetchBusinessPageDetails, success={response.success}')
        return response

    # endregion

    # region product management module
    def createProduct(self, request, context):
        print(f' createProduct')
        response = gb_service_pb2.CreateProduct.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_business_page = db.get_business_page(business_page_id=request.businessPageId)

        if None not in [gb_user, gb_business_page]:
            db.create_product(gb_user=gb_user, gb_business_page=gb_business_page, name=request.name, picture_blob=request.pictureBlob)
            response.success = True

        print(f' createProduct, success={response.success}')
        return response

    def updateProductDetails(self, request, context):
        print(f' updateProductDetails')
        # todo update product details
        print(f' updateProductDetails')

    def uncreateProduct(self, request, context):
        print(f' uncreateProduct')
        # todo uncreate product
        print(f' uncreateProduct')

    def publishProduct(self, request, context):
        print(f' publishProduct')
        # todo publish product
        print(f' publishProduct')

    def unpublishProduct(self, request, context):
        print(f' unpublishProduct')
        # todo unpublish product
        print(f' unpublishProduct')

    def fetchBusinessPageProductIds(self, request, context):
        print(f' fetchBusinessPageProductIds')
        response = gb_service_pb2.FetchBusinessPageProductIds.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_business_page = db.get_business_page(business_page_id=request.businessPageId)

        if None not in [gb_user, gb_business_page]:
            response.id.extend(db.get_business_page_product_ids(gb_business_page=gb_business_page))
            response.success = True

        print(f' fetchBusinessPageProductIds, success={response.success}')
        return response

    def fetchProductDetails(self, request, context):
        print(f' fetchProductDetails')
        response = gb_service_pb2.FetchProductDetails.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_product = db.get_product(product_id=request.productId)
        if None not in [gb_user, gb_product]:
            response.id = gb_product['id']
            response.name = gb_product['name']
            response.published = gb_product['published']
            response.pictureBlob = bytes(gb_product['pictureBlob'])
            response.success = True

        print(f' fetchProductDetails, success={response.success}')
        return response

    # endregion

    # region purchase management module
    def logPurchase(self, request, context):
        print(f' logPurchase')
        # todo log purchase
        print(f' logPurchase')

    def fetchPurchases(self, request, context):
        print(f' fetchPurchases')
        # todo fetch purchases
        print(f' fetchPurchases')

    def fetchPurchaseDetails(self, request, context):
        print(f' fetchPurchaseDetails')
        # todo fetch purchase details
        print(f' fetchPurchaseDetails')

    # endregion


if __name__ == '__main__':
    print('Starting gRPC server on port 50053.')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gb_service_pb2_grpc.add_GlobensServiceServicer_to_server(servicer=GlobensServiceServicer(), server=server)
    server.add_insecure_port('0.0.0.0:50053')  # TODO: check the address!!!
    server.start()

    try:
        # since server.start() will not block, a sleep-loop is added to keep alive
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
        db.end()
        print('Server has stopped.')
