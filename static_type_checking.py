from typing import List


class MyType:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


def my_multiply_func(a: int, b: int) -> int:
    return a * b


def multiply_MyType(ab: MyType) -> int:
    return ab.a * ab.b


my_multiply_func(8, 8)

my_type = MyType(6, 6)
multiply_MyType(my_type)

# my_var = 8

# def multiply_MyType_2(ab):
#     return ab.a * ab.b

# print (f"my var: {my_var}")

# class Fact():
#     def __init__(self, name: str, description: str, truth_deps: List, base_truth: bool = False, truth_score: float = 0):
#         self.name = name
#         self.description = description
#         self.base_truth: bool = base_truth
#         self.truth_denendancies: List[Fact] = truth_deps
#         self.truth_score: float = truth_score if base_truth else self.calc_truth_score(truth_deps)
#         self.truth_class: str = self.get_truth_class(self.truth_score)

#     def __str__(self) -> str:
#         return f"Fact with: \n Score {self.truth_score} \n {self.truth_class}"

#     def __add__(self, fact):
#         print("CREATE NEW FACT")
#         print (fact.truth_denendancies)
#         print (self.truth_denendancies)
#         return Fact(
#             self.name + fact.name,
#             '',
#             [self + fact]
#         )

#     def calc_truth_score(self, deps: List) -> float:
#         print(deps)
#         sum_scores = 0
#         for fact in deps:
#             sum_scores += fact.truth_score
#         return sum_scores / len(deps)


#     def get_truth_class(self, score: float) -> str:
#         classes = {
#             -100: "False",
#             -50: "ProbablyFalse",
#             -25: "PossiblyFalse",
#             0: "NoClearEvidence",
#             10: "PossiblyTrue",
#             25: "SomeEvidence",
#             75: "ReasonableConsensus",
#             90: "LikelyTrue",
#             95: "HighlyLikelyTrue",
#             99: "Near Certain",
#             100: "Certain"
#         }
#         for key, val  in classes.items():
#             if score <= key:
#                 return val
#         else:
#             raise Exception("Truth Class Not Found")


# factA: Fact = Fact('factA', '', [], True,  100)
# factB: Fact = Fact('factB', '', [], True,  100)

# factC: Fact = Fact('factC', '', [factA, factB])
# print(factA.truth_denendancies)
# print(factC)
# print(factA + factB)
