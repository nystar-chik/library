from rest_framework import generics, mixins

class ProMixinsGenericsAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    pass

class ProMixinsDetailGenericsAPI(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    pass