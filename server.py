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
        # todo deactivate user
        pass

    def updateUserDetails(self, request, context):
        # todo update user details
        pass

    def fetchUserDetails(self, request, context):
        # todo fetch user details
        pass

    # endregion

    # region vacancy management module
    def createVacancy(self, request, context):
        # todo create vacancy
        pass

    def updateVacancyDetails(self, request, context):
        # todo update vacancy details
        pass

    def uncreateVacancy(self, request, context):
        # todo uncreate vacancy
        pass

    def fetchVacancies(self, request, context):
        # todo fetch vacancies
        pass

    def fetchVacancyDetails(self, request, context):
        # todo fetch vacancy details
        pass

    # endregion

    # region vacancy application management module
    def createVacancyApplication(self, request, context):
        # todo create vacancy application
        pass

    def updateVacancyApplicationDetails(self, request, context):
        # todo update vacancy application
        pass

    def uncreateVacancyApplication(self, request, context):
        # todo uncreate vacancy application
        pass

    def fetchMyVacancyApplications(self, request, context):
        # todo fetch my vacancy applications
        pass

    def fetchVacancyApplicationDetails(self, request, context):
        # todo fetch vacancy application details
        pass

    # endregion

    # region business page management module
    def createBusinessPage(self, request, context):
        response = gb_service_pb2.CreateBusinessPage.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)

        if gb_user is not None:
            db.create_business_page(gb_user=gb_user, title=request.title, picture_blob=request.pictureBlob)
            response.success = True

        print(f' createBusinessPage, success={response.success}')
        return response

    def updateBusinessPageDetails(self, request, context):
        # todo update business page details
        pass

    def uncreateBusinessPage(self, request, context):
        # todo uncreate business page
        pass

    def fetchBusinessPages(self, request, context):
        response = gb_service_pb2.FetchBusinessPages.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)

        if gb_user is not None:
            for gb_business_page, gb_vacancy in db.get_business_pages(gb_user=gb_user):
                response.id.extend([gb_business_page['id']])
                response.title.extend([gb_business_page['title']])
                response.type.extend([gb_business_page['type']])
                response.pictureBlob.extend([bytes(gb_business_page['pictureBlob'])])
                response.role.extend([gb_vacancy['role']])
            response.success = True

        # print(f' fetchBusinessPages, success={response.success}')
        return response

    def fetchBusinessPageDetails(self, request, context):
        # todo fetch business page details
        pass

    # endregion

    # region product management module
    def createProduct(self, request, context):
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
        # todo update product details
        pass

    def uncreateProduct(self, request, context):
        # todo uncreate product
        pass

    def publishProduct(self, request, context):
        # todo publish product
        pass

    def unpublishProduct(self, request, context):
        # todo unpublish product
        pass

    def fetchProducts(self, request, context):
        response = gb_service_pb2.FetchProducts.Response()
        response.success = False

        gb_user = db.get_user(session_key=request.sessionKey)
        gb_business_page = db.get_business_page(business_page_id=request.businessPageId)

        if None not in [gb_user, gb_business_page]:
            for gb_product in db.get_products(gb_business_page=gb_business_page):
                response.id.extend([gb_product['id']])
                response.name.extend([gb_product['name']])
                response.published.extend([gb_product['published']])
                response.pictureBlob.extend([bytes(gb_product['pictureBlob'])])
            response.success = True

        # print(f' fetchProducts, success={response.success}')
        return response

    def fetchProductDetails(self, request, context):
        # todo fetch product details
        pass

    # endregion

    # region purchase management module
    def logPurchase(self, request, context):
        # todo log purchase
        pass

    def fetchPurchases(self, request, context):
        # todo fetch purchases
        pass

    def fetchPurchaseDetails(self, request, context):
        # todo fetch purchase details
        pass

    # endregion

    # region test proto (rpc)
    def testSum(self, request, context):
        res = gb_service_pb2.TestSum.Response()
        res.c = request.a + request.b
        return res
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
