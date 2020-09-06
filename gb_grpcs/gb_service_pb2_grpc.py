# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import gb_service_pb2 as gb__service__pb2


class GlobensServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.authenticateUser = channel.unary_unary(
            '/GlobensService/authenticateUser',
            request_serializer=gb__service__pb2.AuthenticateUser.Request.SerializeToString,
            response_deserializer=gb__service__pb2.AuthenticateUser.Response.FromString,
        )
        self.deactivateUser = channel.unary_unary(
            '/GlobensService/deactivateUser',
            request_serializer=gb__service__pb2.DeactivateUser.Request.SerializeToString,
            response_deserializer=gb__service__pb2.DeactivateUser.Response.FromString,
        )
        self.updateUserDetails = channel.unary_unary(
            '/GlobensService/updateUserDetails',
            request_serializer=gb__service__pb2.UpdateUserDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UpdateUserDetails.Response.FromString,
        )
        self.fetchUserDetails = channel.unary_unary(
            '/GlobensService/fetchUserDetails',
            request_serializer=gb__service__pb2.FetchUserDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchUserDetails.Response.FromString,
        )
        self.createVacantJob = channel.unary_unary(
            '/GlobensService/createVacantJob',
            request_serializer=gb__service__pb2.CreateVacantJob.Request.SerializeToString,
            response_deserializer=gb__service__pb2.CreateVacantJob.Response.FromString,
        )
        self.updateJobDetails = channel.unary_unary(
            '/GlobensService/updateJobDetails',
            request_serializer=gb__service__pb2.UpdateJobDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UpdateJobDetails.Response.FromString,
        )
        self.uncreateJob = channel.unary_unary(
            '/GlobensService/uncreateJob',
            request_serializer=gb__service__pb2.UncreateJob.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UncreateJob.Response.FromString,
        )
        self.fetchBusinessPageJobIds = channel.unary_unary(
            '/GlobensService/fetchBusinessPageJobIds',
            request_serializer=gb__service__pb2.FetchBusinessPageJobIds.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchBusinessPageJobIds.Response.FromString,
        )
        self.fetchNextKVacantJobIds = channel.unary_unary(
            '/GlobensService/fetchNextKVacantJobIds',
            request_serializer=gb__service__pb2.FetchNextKVacantJobIds.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchNextKVacantJobIds.Response.FromString,
        )
        self.fetchJobDetails = channel.unary_unary(
            '/GlobensService/fetchJobDetails',
            request_serializer=gb__service__pb2.FetchJobDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchJobDetails.Response.FromString,
        )
        self.createVacancyApplication = channel.unary_unary(
            '/GlobensService/createVacancyApplication',
            request_serializer=gb__service__pb2.CreateVacancyApplication.Request.SerializeToString,
            response_deserializer=gb__service__pb2.CreateVacancyApplication.Response.FromString,
        )
        self.updateVacancyApplicationDetails = channel.unary_unary(
            '/GlobensService/updateVacancyApplicationDetails',
            request_serializer=gb__service__pb2.UpdateVacancyApplicationDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UpdateVacancyApplicationDetails.Response.FromString,
        )
        self.uncreateVacancyApplication = channel.unary_unary(
            '/GlobensService/uncreateVacancyApplication',
            request_serializer=gb__service__pb2.UncreateVacancyApplication.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UncreateVacancyApplication.Response.FromString,
        )
        self.fetchMyVacancyApplicationIds = channel.unary_unary(
            '/GlobensService/fetchMyVacancyApplicationIds',
            request_serializer=gb__service__pb2.FetchMyVacancyApplicationIds.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchMyVacancyApplicationIds.Response.FromString,
        )
        self.fetchVacancyApplicationDetails = channel.unary_unary(
            '/GlobensService/fetchVacancyApplicationDetails',
            request_serializer=gb__service__pb2.FetchVacancyApplicationDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchVacancyApplicationDetails.Response.FromString,
        )
        self.createBusinessPage = channel.unary_unary(
            '/GlobensService/createBusinessPage',
            request_serializer=gb__service__pb2.CreateBusinessPage.Request.SerializeToString,
            response_deserializer=gb__service__pb2.CreateBusinessPage.Response.FromString,
        )
        self.updateBusinessPageDetails = channel.unary_unary(
            '/GlobensService/updateBusinessPageDetails',
            request_serializer=gb__service__pb2.UpdateBusinessPageDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UpdateBusinessPageDetails.Response.FromString,
        )
        self.uncreateBusinessPage = channel.unary_unary(
            '/GlobensService/uncreateBusinessPage',
            request_serializer=gb__service__pb2.UncreateBusinessPage.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UncreateBusinessPage.Response.FromString,
        )
        self.fetchMyBusinessPageIds = channel.unary_unary(
            '/GlobensService/fetchMyBusinessPageIds',
            request_serializer=gb__service__pb2.FetchMyBusinessPageIds.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchMyBusinessPageIds.Response.FromString,
        )
        self.fetchBusinessPageDetails = channel.unary_unary(
            '/GlobensService/fetchBusinessPageDetails',
            request_serializer=gb__service__pb2.FetchBusinessPageDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchBusinessPageDetails.Response.FromString,
        )
        self.createProduct = channel.unary_unary(
            '/GlobensService/createProduct',
            request_serializer=gb__service__pb2.CreateProduct.Request.SerializeToString,
            response_deserializer=gb__service__pb2.CreateProduct.Response.FromString,
        )
        self.updateProductDetails = channel.unary_unary(
            '/GlobensService/updateProductDetails',
            request_serializer=gb__service__pb2.UpdateProductDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UpdateProductDetails.Response.FromString,
        )
        self.publishProduct = channel.unary_unary(
            '/GlobensService/publishProduct',
            request_serializer=gb__service__pb2.PublishProduct.Request.SerializeToString,
            response_deserializer=gb__service__pb2.PublishProduct.Response.FromString,
        )
        self.unpublishProduct = channel.unary_unary(
            '/GlobensService/unpublishProduct',
            request_serializer=gb__service__pb2.UnpublishProduct.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UnpublishProduct.Response.FromString,
        )
        self.uncreateProduct = channel.unary_unary(
            '/GlobensService/uncreateProduct',
            request_serializer=gb__service__pb2.UncreateProduct.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UncreateProduct.Response.FromString,
        )
        self.fetchBusinessPageProducts = channel.unary_unary(
            '/GlobensService/fetchBusinessPageProducts',
            request_serializer=gb__service__pb2.FetchBusinessPageProducts.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchBusinessPageProducts.Response.FromString,
        )
        self.fetchProductDetails = channel.unary_unary(
            '/GlobensService/fetchProductDetails',
            request_serializer=gb__service__pb2.FetchProductDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchProductDetails.Response.FromString,
        )
        self.logPurchase = channel.unary_unary(
            '/GlobensService/logPurchase',
            request_serializer=gb__service__pb2.LogPurchase.Request.SerializeToString,
            response_deserializer=gb__service__pb2.LogPurchase.Response.FromString,
        )
        self.fetchPurchases = channel.unary_unary(
            '/GlobensService/fetchPurchases',
            request_serializer=gb__service__pb2.FetchPurchases.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchPurchases.Response.FromString,
        )
        self.fetchPurchaseDetails = channel.unary_unary(
            '/GlobensService/fetchPurchaseDetails',
            request_serializer=gb__service__pb2.FetchPurchaseDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchPurchaseDetails.Response.FromString,
        )


class GlobensServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def authenticateUser(self, request, context):
        """user management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deactivateUser(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateUserDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchUserDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createVacantJob(self, request, context):
        """vacancy management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateJobDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def uncreateJob(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchBusinessPageJobIds(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchNextKVacantJobIds(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchJobDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createVacancyApplication(self, request, context):
        """vacancy application management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateVacancyApplicationDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def uncreateVacancyApplication(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchMyVacancyApplicationIds(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchVacancyApplicationDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createBusinessPage(self, request, context):
        """business page management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateBusinessPageDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def uncreateBusinessPage(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchMyBusinessPageIds(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchBusinessPageDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createProduct(self, request, context):
        """product management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateProductDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def publishProduct(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unpublishProduct(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def uncreateProduct(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchBusinessPageProducts(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchProductDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logPurchase(self, request, context):
        """purchase management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchPurchases(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchPurchaseDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GlobensServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'authenticateUser': grpc.unary_unary_rpc_method_handler(
            servicer.authenticateUser,
            request_deserializer=gb__service__pb2.AuthenticateUser.Request.FromString,
            response_serializer=gb__service__pb2.AuthenticateUser.Response.SerializeToString,
        ),
        'deactivateUser': grpc.unary_unary_rpc_method_handler(
            servicer.deactivateUser,
            request_deserializer=gb__service__pb2.DeactivateUser.Request.FromString,
            response_serializer=gb__service__pb2.DeactivateUser.Response.SerializeToString,
        ),
        'updateUserDetails': grpc.unary_unary_rpc_method_handler(
            servicer.updateUserDetails,
            request_deserializer=gb__service__pb2.UpdateUserDetails.Request.FromString,
            response_serializer=gb__service__pb2.UpdateUserDetails.Response.SerializeToString,
        ),
        'fetchUserDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchUserDetails,
            request_deserializer=gb__service__pb2.FetchUserDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchUserDetails.Response.SerializeToString,
        ),
        'createVacantJob': grpc.unary_unary_rpc_method_handler(
            servicer.createVacantJob,
            request_deserializer=gb__service__pb2.CreateVacantJob.Request.FromString,
            response_serializer=gb__service__pb2.CreateVacantJob.Response.SerializeToString,
        ),
        'updateJobDetails': grpc.unary_unary_rpc_method_handler(
            servicer.updateJobDetails,
            request_deserializer=gb__service__pb2.UpdateJobDetails.Request.FromString,
            response_serializer=gb__service__pb2.UpdateJobDetails.Response.SerializeToString,
        ),
        'uncreateJob': grpc.unary_unary_rpc_method_handler(
            servicer.uncreateJob,
            request_deserializer=gb__service__pb2.UncreateJob.Request.FromString,
            response_serializer=gb__service__pb2.UncreateJob.Response.SerializeToString,
        ),
        'fetchBusinessPageJobIds': grpc.unary_unary_rpc_method_handler(
            servicer.fetchBusinessPageJobIds,
            request_deserializer=gb__service__pb2.FetchBusinessPageJobIds.Request.FromString,
            response_serializer=gb__service__pb2.FetchBusinessPageJobIds.Response.SerializeToString,
        ),
        'fetchNextKVacantJobIds': grpc.unary_unary_rpc_method_handler(
            servicer.fetchNextKVacantJobIds,
            request_deserializer=gb__service__pb2.FetchNextKVacantJobIds.Request.FromString,
            response_serializer=gb__service__pb2.FetchNextKVacantJobIds.Response.SerializeToString,
        ),
        'fetchJobDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchJobDetails,
            request_deserializer=gb__service__pb2.FetchJobDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchJobDetails.Response.SerializeToString,
        ),
        'createVacancyApplication': grpc.unary_unary_rpc_method_handler(
            servicer.createVacancyApplication,
            request_deserializer=gb__service__pb2.CreateVacancyApplication.Request.FromString,
            response_serializer=gb__service__pb2.CreateVacancyApplication.Response.SerializeToString,
        ),
        'updateVacancyApplicationDetails': grpc.unary_unary_rpc_method_handler(
            servicer.updateVacancyApplicationDetails,
            request_deserializer=gb__service__pb2.UpdateVacancyApplicationDetails.Request.FromString,
            response_serializer=gb__service__pb2.UpdateVacancyApplicationDetails.Response.SerializeToString,
        ),
        'uncreateVacancyApplication': grpc.unary_unary_rpc_method_handler(
            servicer.uncreateVacancyApplication,
            request_deserializer=gb__service__pb2.UncreateVacancyApplication.Request.FromString,
            response_serializer=gb__service__pb2.UncreateVacancyApplication.Response.SerializeToString,
        ),
        'fetchMyVacancyApplicationIds': grpc.unary_unary_rpc_method_handler(
            servicer.fetchMyVacancyApplicationIds,
            request_deserializer=gb__service__pb2.FetchMyVacancyApplicationIds.Request.FromString,
            response_serializer=gb__service__pb2.FetchMyVacancyApplicationIds.Response.SerializeToString,
        ),
        'fetchVacancyApplicationDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchVacancyApplicationDetails,
            request_deserializer=gb__service__pb2.FetchVacancyApplicationDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchVacancyApplicationDetails.Response.SerializeToString,
        ),
        'createBusinessPage': grpc.unary_unary_rpc_method_handler(
            servicer.createBusinessPage,
            request_deserializer=gb__service__pb2.CreateBusinessPage.Request.FromString,
            response_serializer=gb__service__pb2.CreateBusinessPage.Response.SerializeToString,
        ),
        'updateBusinessPageDetails': grpc.unary_unary_rpc_method_handler(
            servicer.updateBusinessPageDetails,
            request_deserializer=gb__service__pb2.UpdateBusinessPageDetails.Request.FromString,
            response_serializer=gb__service__pb2.UpdateBusinessPageDetails.Response.SerializeToString,
        ),
        'uncreateBusinessPage': grpc.unary_unary_rpc_method_handler(
            servicer.uncreateBusinessPage,
            request_deserializer=gb__service__pb2.UncreateBusinessPage.Request.FromString,
            response_serializer=gb__service__pb2.UncreateBusinessPage.Response.SerializeToString,
        ),
        'fetchMyBusinessPageIds': grpc.unary_unary_rpc_method_handler(
            servicer.fetchMyBusinessPageIds,
            request_deserializer=gb__service__pb2.FetchMyBusinessPageIds.Request.FromString,
            response_serializer=gb__service__pb2.FetchMyBusinessPageIds.Response.SerializeToString,
        ),
        'fetchBusinessPageDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchBusinessPageDetails,
            request_deserializer=gb__service__pb2.FetchBusinessPageDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchBusinessPageDetails.Response.SerializeToString,
        ),
        'createProduct': grpc.unary_unary_rpc_method_handler(
            servicer.createProduct,
            request_deserializer=gb__service__pb2.CreateProduct.Request.FromString,
            response_serializer=gb__service__pb2.CreateProduct.Response.SerializeToString,
        ),
        'updateProductDetails': grpc.unary_unary_rpc_method_handler(
            servicer.updateProductDetails,
            request_deserializer=gb__service__pb2.UpdateProductDetails.Request.FromString,
            response_serializer=gb__service__pb2.UpdateProductDetails.Response.SerializeToString,
        ),
        'publishProduct': grpc.unary_unary_rpc_method_handler(
            servicer.publishProduct,
            request_deserializer=gb__service__pb2.PublishProduct.Request.FromString,
            response_serializer=gb__service__pb2.PublishProduct.Response.SerializeToString,
        ),
        'unpublishProduct': grpc.unary_unary_rpc_method_handler(
            servicer.unpublishProduct,
            request_deserializer=gb__service__pb2.UnpublishProduct.Request.FromString,
            response_serializer=gb__service__pb2.UnpublishProduct.Response.SerializeToString,
        ),
        'uncreateProduct': grpc.unary_unary_rpc_method_handler(
            servicer.uncreateProduct,
            request_deserializer=gb__service__pb2.UncreateProduct.Request.FromString,
            response_serializer=gb__service__pb2.UncreateProduct.Response.SerializeToString,
        ),
        'fetchBusinessPageProducts': grpc.unary_unary_rpc_method_handler(
            servicer.fetchBusinessPageProducts,
            request_deserializer=gb__service__pb2.FetchBusinessPageProducts.Request.FromString,
            response_serializer=gb__service__pb2.FetchBusinessPageProducts.Response.SerializeToString,
        ),
        'fetchProductDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchProductDetails,
            request_deserializer=gb__service__pb2.FetchProductDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchProductDetails.Response.SerializeToString,
        ),
        'logPurchase': grpc.unary_unary_rpc_method_handler(
            servicer.logPurchase,
            request_deserializer=gb__service__pb2.LogPurchase.Request.FromString,
            response_serializer=gb__service__pb2.LogPurchase.Response.SerializeToString,
        ),
        'fetchPurchases': grpc.unary_unary_rpc_method_handler(
            servicer.fetchPurchases,
            request_deserializer=gb__service__pb2.FetchPurchases.Request.FromString,
            response_serializer=gb__service__pb2.FetchPurchases.Response.SerializeToString,
        ),
        'fetchPurchaseDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchPurchaseDetails,
            request_deserializer=gb__service__pb2.FetchPurchaseDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchPurchaseDetails.Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'GlobensService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
