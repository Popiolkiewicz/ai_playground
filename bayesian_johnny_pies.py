from enum import Enum
import pandas as pd


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


class BayesianJohnnyPies:
    df = pd.DataFrame({'decision': [True, True, True, True, True, True, False, False, False, False, False, False],
                       'Shape': [Shape.CIRCLE, Shape.CIRCLE, Shape.TRIANGLE, Shape.TRIANGLE, Shape.TRIANGLE,
                                 Shape.SQUARE, Shape.CIRCLE, Shape.TRIANGLE, Shape.CIRCLE, Shape.CIRCLE, Shape.SQUARE,
                                 Shape.SQUARE],
                       'CrustSize': [CrustSize.THICK, CrustSize.THIN, CrustSize.THIN, CrustSize.THIN,
                                     CrustSize.THICK, CrustSize.THIN, CrustSize.THIN, CrustSize.THIN,
                                     CrustSize.THIN, CrustSize.THICK, CrustSize.THIN, CrustSize.THICK],
                       'CrustShade': [CrustShade.DARK, CrustShade.DARK, CrustShade.WHITE, CrustShade.DARK,
                                      CrustShade.GRAY, CrustShade.GRAY, CrustShade.GRAY, CrustShade.DARK,
                                      CrustShade.WHITE, CrustShade.DARK, CrustShade.WHITE, CrustShade.WHITE],
                       'FillingSize': [FillingSize.THICK, FillingSize.THIN, FillingSize.THICK, FillingSize.THIN,
                                       FillingSize.THICK, FillingSize.THIN, FillingSize.THICK, FillingSize.THICK,
                                       FillingSize.THICK, FillingSize.THIN, FillingSize.THIN, FillingSize.THICK],
                       'FillingShade': [FillingShade.GRAY, FillingShade.DARK, FillingShade.GRAY, FillingShade.DARK,
                                        FillingShade.DARK, FillingShade.WHITE, FillingShade.DARK, FillingShade.WHITE,
                                        FillingShade.DARK, FillingShade.DARK, FillingShade.GRAY, FillingShade.DARK]},
                      columns=['decision', 'Shape', 'CrustSize', 'CrustShade', 'FillingSize', 'FillingShade'])
    p_dict = {}
    n_dict = {}
    trainingSize = 6

    def run(self):
        gb = self.df.groupby('decision')
        
        ttg = gb.get_group(True).sample(frac=self.trainingSize / 6)

        self.p_dict[Shape.SQUARE] = ttg[ttg['Shape'] == Shape.SQUARE]['Shape'].count() / self.trainingSize
        self.p_dict[Shape.TRIANGLE] = ttg[ttg['Shape'] == Shape.TRIANGLE]['Shape'].count() / self.trainingSize
        self.p_dict[Shape.CIRCLE] = ttg[ttg['Shape'] == Shape.CIRCLE]['Shape'].count() / self.trainingSize

        self.p_dict[CrustSize.THIN] = ttg[ttg['CrustSize'] == CrustSize.THIN]['CrustSize'].count() / self.trainingSize
        self.p_dict[CrustSize.THICK] = ttg[ttg['CrustSize'] == CrustSize.THICK]['CrustSize'].count() / self.trainingSize
        self.p_dict[CrustShade.DARK] = ttg[ttg['CrustShade'] == CrustShade.DARK]['CrustShade'].count() / self.trainingSize
        self.p_dict[CrustShade.GRAY] = ttg[ttg['CrustShade'] == CrustShade.GRAY]['CrustShade'].count() / self.trainingSize
        self.p_dict[CrustShade.WHITE] = ttg[ttg['CrustShade'] == CrustShade.WHITE]['CrustShade'].count() / self.trainingSize

        self.p_dict[FillingSize.THIN] = ttg[ttg['FillingSize'] == FillingSize.THIN]['FillingSize'].count() / self.trainingSize
        self.p_dict[FillingSize.THICK] = ttg[ttg['FillingSize'] == FillingSize.THICK]['FillingSize'].count() / self.trainingSize
        self.p_dict[FillingShade.DARK] = ttg[ttg['FillingShade'] == FillingShade.DARK]['FillingShade'].count() / self.trainingSize
        self.p_dict[FillingShade.GRAY] = ttg[ttg['FillingShade'] == FillingShade.GRAY]['FillingShade'].count() / self.trainingSize
        self.p_dict[FillingShade.WHITE] = ttg[ttg['FillingShade'] == FillingShade.WHITE]['FillingShade'].count() / self.trainingSize

        for x, y in self.p_dict.items():
            print(x, y)
            
        ftg = gb.get_group(False).sample(frac=self.trainingSize / 6)

        self.n_dict[Shape.SQUARE] = ftg[ftg['Shape'] == Shape.SQUARE]['Shape'].count() / self.trainingSize
        self.n_dict[Shape.TRIANGLE] = ftg[ftg['Shape'] == Shape.TRIANGLE]['Shape'].count() / self.trainingSize
        self.n_dict[Shape.CIRCLE] = ftg[ftg['Shape'] == Shape.CIRCLE]['Shape'].count() / self.trainingSize

        self.n_dict[CrustSize.THIN] = ftg[ftg['CrustSize'] == CrustSize.THIN]['CrustSize'].count() / self.trainingSize
        self.n_dict[CrustSize.THICK] = ftg[ftg['CrustSize'] == CrustSize.THICK]['CrustSize'].count() / self.trainingSize
        self.n_dict[CrustShade.DARK] = ftg[ftg['CrustShade'] == CrustShade.DARK]['CrustShade'].count() / self.trainingSize
        self.n_dict[CrustShade.GRAY] = ftg[ftg['CrustShade'] == CrustShade.GRAY]['CrustShade'].count() / self.trainingSize
        self.n_dict[CrustShade.WHITE] = ftg[ftg['CrustShade'] == CrustShade.WHITE]['CrustShade'].count() / self.trainingSize

        self.n_dict[FillingSize.THIN] = ftg[ftg['FillingSize'] == FillingSize.THIN]['FillingSize'].count() / self.trainingSize
        self.n_dict[FillingSize.THICK] = ftg[ftg['FillingSize'] == FillingSize.THICK]['FillingSize'].count() / self.trainingSize
        self.n_dict[FillingShade.DARK] = ftg[ftg['FillingShade'] == FillingShade.DARK]['FillingShade'].count() / self.trainingSize
        self.n_dict[FillingShade.GRAY] = ftg[ftg['FillingShade'] == FillingShade.GRAY]['FillingShade'].count() / self.trainingSize
        self.n_dict[FillingShade.WHITE] = ftg[ftg['FillingShade'] == FillingShade.WHITE]['FillingShade'].count() / self.trainingSize

        for x, y in self.n_dict.items():
            print(x, y)

BayesianJohnnyPies().run()
