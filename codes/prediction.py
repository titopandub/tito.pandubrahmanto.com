# class Prediction():
#     def __init__(self, user_id):
#         self.user_id = user_id

#     def results(self):
#         seed = Seed.data(self.user_id)
#         predictions = Model.predict(seed)

#         if len(predictions) <= 10:
#             predictions += Fallback.result()

#         return predictions

# class Prediction():
#     def __init__(self, user_id):
#         self.user_id = user_id

#     def results(self, special=False):
#         seed = Seed.data(self.user_id)
#         predictions = Model.predict(seed)

#         if special:
#             predictions = Special.filter(predictions)

#         if len(predictions) <= 10:
#             predictions += Fallback.result()

#         return predictions

# class Prediction():
#     def __init__(self, user_id):
#         self.user_id = user_id

#     def results(self, special=False):
#         seed = Seed.data(self.user_id)
#         predictions = Model.predict(seed)

#         if special:
#             predictions = Special.filter(predictions)

#         if len(predictions) <= 10:
#             predictions += self.fallback(special)

#         return predictions

#     def fallback(self, special=False):
#         if special:
#             return FallbackSpecial.result()
#         else:
#             return Fallback.result()

# class Prediction():
#     def __init__(self, user_id):
#         self.user_id = user_id

#     def results(self):
#         seed = Seed.data(self.user_id)
#         predictions = Model.predict(seed)

#         if len(predictions) <= 10:
#             predictions += self.fallback()

#         return predictions

#     def fallback(self):
#         return Fallback.result()

# class PredictionSpecial():
#     def __init__(self, user_id):
#         self.user_id = user_id

#     def results(self):
#         seed = Seed.data(self.user_id)
#         predictions = Model.predict(seed)

#         predictions = Special.filter(predictions)

#         if len(predictions) <= 10:
#             predictions += self.fallback()

#         return predictions

#     def fallback(self):
#         return FallbackSpecial.result()


class Prediction():
    def __init__(self, user_id):
        self.user_id = user_id

    def results(self):
        seed = Seed.data(self.user_id)
        predictions = Model.predict(seed)

        predictions = self.filter(predictions)

        if len(predictions) <= 10:
            predictions += self.fallback()

        return predictions

    def filter(self, predictions):
        return predictions

    def fallback(self):
        return Fallback.result()

class PredictionSpecial(Prediction):
    def filter(self, predictions):
        return Special.filter(predictions)

    def fallback(self):
        return FallbackSpecial.result()

class FallbackSpecial:
    def result():
        return [17, 19, 21]

class Special:
    def filter(predictions):
        return [x for x in predictions if x % 2 == 0]

class Seed:
    def data(user_id):
        return [1, 2, 3, 4, 5]

class Model:
    def predict(seed):
        return [6, 7, 8, 9, 10]

class Fallback:
    def result():
        return [11, 12, 13, 14, 15]


user_id = 1
print(Prediction(user_id).results())
print(PredictionSpecial(user_id).results())