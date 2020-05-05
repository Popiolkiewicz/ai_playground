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
    condProb = {}
    p_dict = {}
    n_dict = {}
    trainingSize = 5
    dataSize = 6

    def run(self):
        gb = self.df.groupby('decision')
        fg = gb.get_group(False).sample(frac=1)
        tg = gb.get_group(True).sample(frac=1)

        trueTrainingDf = tg[:self.trainingSize]
        falseTrainingDf = fg[:self.trainingSize]

        testData = pd.concat([tg[self.trainingSize:self.dataSize], fg[self.trainingSize:self.dataSize]])

        self.createConditionalProbabilities(trueTrainingDf, falseTrainingDf)

        # print(self.n_dict)
        # print(self.p_dict)

        self.test(testData)

    def createConditionalProbabilities(self, ttg, ftg):
        for piePropertyEnum in self.getPiePropertyEnums():
            for data in piePropertyEnum:
                self.p_dict[data] = ttg[ttg[piePropertyEnum.__name__] == data].shape[0] / self.trainingSize
                self.n_dict[data] = ftg[ftg[piePropertyEnum.__name__] == data].shape[0] / self.trainingSize

    def getPiePropertyEnums(self):
        return [Shape, CrustSize, CrustShade, FillingSize, FillingShade]

    def test(self, testData):
        for idx in range(testData.shape[0]):
            testRow = testData.iloc[idx]
            decision = testRow['decision']
            falseProbability = 1
            trueProbability = 1
            for piePropertyEnum in self.getPiePropertyEnums():
                name = piePropertyEnum.__name__
                falseProbability *= self.n_dict[testRow[name]]
                trueProbability *= self.p_dict[testRow[name]]
            print(f'falseProbability: {falseProbability}')
            print(f'trueProbability: {trueProbability}')
            print(f'testRowDecision: {decision}')
            if ((falseProbability < trueProbability and testRow['decision'] == True) or
                    (falseProbability > trueProbability and testRow['decision'] == False)):
                print('Success')
            else:
                print('Failure')


BayesianJohnnyPies().run()
