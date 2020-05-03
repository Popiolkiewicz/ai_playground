from enum import Enum


class Shape(Enum):
    CIRCLE = 1
    TRIANGLE = 2
    SQUARE = 3


class CrustSize(Enum):
    THICK = 1
    THIN = 2


class CrustShade(Enum):
    GRAY = 1
    WHITE = 2
    DARK = 3


class FillingSize(Enum):
    THICK = 1
    THIN = 2


class FillingShade(Enum):
    GRAY = 1
    WHITE = 2
    DARK = 3


class HillClimbingJohnnyPies:
    trainingInput = [[True, Shape.CIRCLE, CrustSize.THICK, CrustShade.DARK, FillingSize.THIN, FillingShade.WHITE],
                     [True, Shape.CIRCLE, CrustSize.THIN, CrustShade.DARK, FillingSize.THICK, FillingShade.GRAY],
                     [True, Shape.TRIANGLE, CrustSize.THIN, CrustShade.WHITE, FillingSize.THIN, FillingShade.DARK],
                     [True, Shape.TRIANGLE, CrustSize.THIN, CrustShade.DARK, FillingSize.THICK, FillingShade.WHITE],
                     [True, Shape.TRIANGLE, CrustSize.THIN, CrustShade.GRAY, FillingSize.THIN, FillingShade.DARK],
                     [True, Shape.SQUARE, CrustSize.THIN, CrustShade.WHITE, FillingSize.THICK, FillingShade.WHITE],
                     [False, Shape.SQUARE, CrustSize.THIN, CrustShade.DARK, FillingSize.THIN, FillingShade.GRAY],
                     [False, Shape.TRIANGLE, CrustSize.THIN, CrustShade.DARK, FillingSize.THICK, FillingShade.DARK],
                     [False, Shape.CIRCLE, CrustSize.THIN, CrustShade.WHITE, FillingSize.THIN, FillingShade.WHITE],
                     [False, Shape.CIRCLE, CrustSize.THICK, CrustShade.WHITE, FillingSize.THICK, FillingShade.GRAY],
                     [False, Shape.SQUARE, CrustSize.THIN, CrustShade.DARK, FillingSize.THICK, FillingShade.DARK],
                     [False, Shape.SQUARE, CrustSize.THIN, CrustShade.GRAY, FillingSize.THIN, FillingShade.GRAY]]

    def run(self):
        for trainingExample in self.trainingInput:
            actual = trainingExample[0]
            evaluated = self.evaluateJohnnyLikesPie(trainingExample)
            print(f'Success?: {actual == evaluated}')

    # evaluate function brute forced for now - just to get the idea (score - 11/12)
    def evaluateJohnnyLikesPie(self, obj):
        return ((obj[1] == Shape.TRIANGLE and obj[2] == CrustSize.THIN)
                or (obj[1] == Shape.CIRCLE and obj[3] == CrustShade.DARK)
                or (obj[1] == Shape.SQUARE and obj[3] == CrustShade.WHITE))


obj = HillClimbingJohnnyPies()
obj.run()
