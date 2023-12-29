from torchvision.transforms import transforms

from lambdaLearn.Base.Transformer import Transformer


class Normalization(Transformer):
    def __init__(self, mean=None, std=None):
        super().__init__()
        """
        :param mean: The mean of normalization.
        :param std: The standard deviation of normalization.
        """
        self.mean = mean
        self.std = std
        self.normalize = transforms.Normalize(mean=self.mean, std=self.std)

    def transform(self, X):
        X = self.normalize(X.float())
        return X
