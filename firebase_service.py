import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirebaseService:
    def __init__(self):
        super().__init__()

        cred = credentials.Certificate(
            'ncu-news-flutter-firebase-adminsdk-1h3yu-7239e1b854.json')
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def addArticleOutline(self, articleOutline):
        doc_ref = self.db.collection(
            'Dcard').document(articleOutline.link.split('/')[-1])
        doc_ref.set(articleOutline.toJSON())
