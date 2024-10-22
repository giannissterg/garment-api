
from pymongo import MongoClient, errors


class PyMongoFactory:
    def __init__(self, uri="mongodb://localhost:27017/", **client_options):
        """
        Initializes the MongoFactory with a default URI and optional MongoClient options.
        You can pass additional options like socketTimeoutMS, retryWrites, etc.
        """
        self.uri = uri
        self.client_options = client_options
        self._client_instance = None  # Instance-level MongoClient reference

    def create(self) -> MongoClient:
        """
        Creates and returns a MongoClient instance with error handling.
        Reuses the client if it was already created (instance-level reuse).
        """
        if self._client_instance is None:
            try:
                # Create a new MongoClient instance only if it hasn't been created yet
                self._client_instance = MongoClient(self.uri, **self.client_options)
                print("MongoClient created")
            except errors.ConnectionError as ce:
                print(f"Error connecting to MongoDB: {ce}")
                return None
            except errors.ConfigurationError as conf_err:
                print(f"Configuration error: {conf_err}")
                return None
        else:
            print("Reusing existing MongoClient")
        return self._client_instance  # Return the existing instance

    def close_client(self):
        """
        Closes the MongoClient instance if it exists.
        """
        if self._client_instance:
            self._client_instance.close()
            self._client_instance = None
            print("MongoClient closed.")
