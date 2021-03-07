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
        self.fetchNextKProductIds = channel.unary_unary(
            '/GlobensService/fetchNextKProductIds',
            request_serializer=gb__service__pb2.FetchNextKProductIds.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchNextKProductIds.Response.FromString,
        )
        self.fetchProductDetails = channel.unary_unary(
            '/GlobensService/fetchProductDetails',
            request_serializer=gb__service__pb2.FetchProductDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchProductDetails.Response.FromString,
        )
        self.fetchProductCategoryIds = channel.unary_unary(
            '/GlobensService/fetchProductCategoryIds',
            request_serializer=gb__service__pb2.FetchProductCategoryIds.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchProductCategoryIds.Response.FromString,
        )
        self.fetchProductCategoryDetails = channel.unary_unary(
            '/GlobensService/fetchProductCategoryDetails',
            request_serializer=gb__service__pb2.FetchProductCategoryDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchProductCategoryDetails.Response.FromString,
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
        self.createJobApplication = channel.unary_unary(
            '/GlobensService/createJobApplication',
            request_serializer=gb__service__pb2.CreateJobApplication.Request.SerializeToString,
            response_deserializer=gb__service__pb2.CreateJobApplication.Response.FromString,
        )
        self.updateJobApplicationDetails = channel.unary_unary(
            '/GlobensService/updateJobApplicationDetails',
            request_serializer=gb__service__pb2.UpdateJobApplicationDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UpdateJobApplicationDetails.Response.FromString,
        )
        self.uncreateJobApplication = channel.unary_unary(
            '/GlobensService/uncreateJobApplication',
            request_serializer=gb__service__pb2.UncreateJobApplication.Request.SerializeToString,
            response_deserializer=gb__service__pb2.UncreateJobApplication.Response.FromString,
        )
        self.fetchJobApplicationIds = channel.unary_unary(
            '/GlobensService/fetchJobApplicationIds',
            request_serializer=gb__service__pb2.FetchJobApplicationIds.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchJobApplicationIds.Response.FromString,
        )
        self.fetchJobApplicationDetails = channel.unary_unary(
            '/GlobensService/fetchJobApplicationDetails',
            request_serializer=gb__service__pb2.FetchJobApplicationDetails.Request.SerializeToString,
            response_deserializer=gb__service__pb2.FetchJobApplicationDetails.Response.FromString,
        )
        self.approveJobApplication = channel.unary_unary(
            '/GlobensService/approveJobApplication',
            request_serializer=gb__service__pb2.ApproveJobApplication.Request.SerializeToString,
            response_deserializer=gb__service__pb2.ApproveJobApplication.Response.FromString,
        )
        self.declineJobApplication = channel.unary_unary(
            '/GlobensService/declineJobApplication',
            request_serializer=gb__service__pb2.DeclineJobApplication.Request.SerializeToString,
            response_deserializer=gb__service__pb2.DeclineJobApplication.Response.FromString,
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
        self.submitProductReview = channel.unary_unary(
            '/GlobensService/submitProductReview',
            request_serializer=gb__service__pb2.SubmitProductReview.Request.SerializeToString,
            response_deserializer=gb__service__pb2.SubmitProductReview.Response.FromString,
        )
        self.retrieveProductReviews = channel.unary_unary(
            '/GlobensService/retrieveProductReviews',
            request_serializer=gb__service__pb2.RetrieveProductReviews.Request.SerializeToString,
            response_deserializer=gb__service__pb2.RetrieveProductReviews.Response.FromString,
        )
        self.editProductReview = channel.unary_unary(
            '/GlobensService/editProductReview',
            request_serializer=gb__service__pb2.EditProductReview.Request.SerializeToString,
            response_deserializer=gb__service__pb2.EditProductReview.Response.FromString,
        )
        self.deleteProductReview = channel.unary_unary(
            '/GlobensService/deleteProductReview',
            request_serializer=gb__service__pb2.DeleteProductReview.Request.SerializeToString,
            response_deserializer=gb__service__pb2.DeleteProductReview.Response.FromString,
        )
        self.submitEmployeeReview = channel.unary_unary(
            '/GlobensService/submitEmployeeReview',
            request_serializer=gb__service__pb2.SubmitEmployeeReview.Request.SerializeToString,
            response_deserializer=gb__service__pb2.SubmitEmployeeReview.Response.FromString,
        )
        self.retrieveEmployeeReviews = channel.unary_unary(
            '/GlobensService/retrieveEmployeeReviews',
            request_serializer=gb__service__pb2.RetrieveEmployeeReviews.Request.SerializeToString,
            response_deserializer=gb__service__pb2.RetrieveEmployeeReviews.Response.FromString,
        )
        self.editEmployeeReview = channel.unary_unary(
            '/GlobensService/editEmployeeReview',
            request_serializer=gb__service__pb2.EditEmployeeReview.Request.SerializeToString,
            response_deserializer=gb__service__pb2.EditEmployeeReview.Response.FromString,
        )
        self.deleteEmployeeReview = channel.unary_unary(
            '/GlobensService/deleteEmployeeReview',
            request_serializer=gb__service__pb2.DeleteEmployeeReview.Request.SerializeToString,
            response_deserializer=gb__service__pb2.DeleteEmployeeReview.Response.FromString,
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

    def fetchNextKProductIds(self, request, context):
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

    def fetchProductCategoryIds(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchProductCategoryDetails(self, request, context):
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

    def createJobApplication(self, request, context):
        """vacancy application management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateJobApplicationDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def uncreateJobApplication(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchJobApplicationIds(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchJobApplicationDetails(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def approveJobApplication(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def declineJobApplication(self, request, context):
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

    def submitProductReview(self, request, context):
        """review management RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def retrieveProductReviews(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def editProductReview(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteProductReview(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def submitEmployeeReview(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def retrieveEmployeeReviews(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def editEmployeeReview(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteEmployeeReview(self, request, context):
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
        'fetchNextKProductIds': grpc.unary_unary_rpc_method_handler(
            servicer.fetchNextKProductIds,
            request_deserializer=gb__service__pb2.FetchNextKProductIds.Request.FromString,
            response_serializer=gb__service__pb2.FetchNextKProductIds.Response.SerializeToString,
        ),
        'fetchProductDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchProductDetails,
            request_deserializer=gb__service__pb2.FetchProductDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchProductDetails.Response.SerializeToString,
        ),
        'fetchProductCategoryIds': grpc.unary_unary_rpc_method_handler(
            servicer.fetchProductCategoryIds,
            request_deserializer=gb__service__pb2.FetchProductCategoryIds.Request.FromString,
            response_serializer=gb__service__pb2.FetchProductCategoryIds.Response.SerializeToString,
        ),
        'fetchProductCategoryDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchProductCategoryDetails,
            request_deserializer=gb__service__pb2.FetchProductCategoryDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchProductCategoryDetails.Response.SerializeToString,
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
        'createJobApplication': grpc.unary_unary_rpc_method_handler(
            servicer.createJobApplication,
            request_deserializer=gb__service__pb2.CreateJobApplication.Request.FromString,
            response_serializer=gb__service__pb2.CreateJobApplication.Response.SerializeToString,
        ),
        'updateJobApplicationDetails': grpc.unary_unary_rpc_method_handler(
            servicer.updateJobApplicationDetails,
            request_deserializer=gb__service__pb2.UpdateJobApplicationDetails.Request.FromString,
            response_serializer=gb__service__pb2.UpdateJobApplicationDetails.Response.SerializeToString,
        ),
        'uncreateJobApplication': grpc.unary_unary_rpc_method_handler(
            servicer.uncreateJobApplication,
            request_deserializer=gb__service__pb2.UncreateJobApplication.Request.FromString,
            response_serializer=gb__service__pb2.UncreateJobApplication.Response.SerializeToString,
        ),
        'fetchJobApplicationIds': grpc.unary_unary_rpc_method_handler(
            servicer.fetchJobApplicationIds,
            request_deserializer=gb__service__pb2.FetchJobApplicationIds.Request.FromString,
            response_serializer=gb__service__pb2.FetchJobApplicationIds.Response.SerializeToString,
        ),
        'fetchJobApplicationDetails': grpc.unary_unary_rpc_method_handler(
            servicer.fetchJobApplicationDetails,
            request_deserializer=gb__service__pb2.FetchJobApplicationDetails.Request.FromString,
            response_serializer=gb__service__pb2.FetchJobApplicationDetails.Response.SerializeToString,
        ),
        'approveJobApplication': grpc.unary_unary_rpc_method_handler(
            servicer.approveJobApplication,
            request_deserializer=gb__service__pb2.ApproveJobApplication.Request.FromString,
            response_serializer=gb__service__pb2.ApproveJobApplication.Response.SerializeToString,
        ),
        'declineJobApplication': grpc.unary_unary_rpc_method_handler(
            servicer.declineJobApplication,
            request_deserializer=gb__service__pb2.DeclineJobApplication.Request.FromString,
            response_serializer=gb__service__pb2.DeclineJobApplication.Response.SerializeToString,
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
        'submitProductReview': grpc.unary_unary_rpc_method_handler(
            servicer.submitProductReview,
            request_deserializer=gb__service__pb2.SubmitProductReview.Request.FromString,
            response_serializer=gb__service__pb2.SubmitProductReview.Response.SerializeToString,
        ),
        'retrieveProductReviews': grpc.unary_unary_rpc_method_handler(
            servicer.retrieveProductReviews,
            request_deserializer=gb__service__pb2.RetrieveProductReviews.Request.FromString,
            response_serializer=gb__service__pb2.RetrieveProductReviews.Response.SerializeToString,
        ),
        'editProductReview': grpc.unary_unary_rpc_method_handler(
            servicer.editProductReview,
            request_deserializer=gb__service__pb2.EditProductReview.Request.FromString,
            response_serializer=gb__service__pb2.EditProductReview.Response.SerializeToString,
        ),
        'deleteProductReview': grpc.unary_unary_rpc_method_handler(
            servicer.deleteProductReview,
            request_deserializer=gb__service__pb2.DeleteProductReview.Request.FromString,
            response_serializer=gb__service__pb2.DeleteProductReview.Response.SerializeToString,
        ),
        'submitEmployeeReview': grpc.unary_unary_rpc_method_handler(
            servicer.submitEmployeeReview,
            request_deserializer=gb__service__pb2.SubmitEmployeeReview.Request.FromString,
            response_serializer=gb__service__pb2.SubmitEmployeeReview.Response.SerializeToString,
        ),
        'retrieveEmployeeReviews': grpc.unary_unary_rpc_method_handler(
            servicer.retrieveEmployeeReviews,
            request_deserializer=gb__service__pb2.RetrieveEmployeeReviews.Request.FromString,
            response_serializer=gb__service__pb2.RetrieveEmployeeReviews.Response.SerializeToString,
        ),
        'editEmployeeReview': grpc.unary_unary_rpc_method_handler(
            servicer.editEmployeeReview,
            request_deserializer=gb__service__pb2.EditEmployeeReview.Request.FromString,
            response_serializer=gb__service__pb2.EditEmployeeReview.Response.SerializeToString,
        ),
        'deleteEmployeeReview': grpc.unary_unary_rpc_method_handler(
            servicer.deleteEmployeeReview,
            request_deserializer=gb__service__pb2.DeleteEmployeeReview.Request.FromString,
            response_serializer=gb__service__pb2.DeleteEmployeeReview.Response.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'GlobensService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
