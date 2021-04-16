from abc import ABC, abstractmethod

class StorageService(ABC):
    @abstractmethod
    def get_processed_results(self):
        pass
    @abstractmethod
    def remove_processed_results(self):
        pass

class s3Storage(StorageService):
    def get_processed_results(self):
        print('Successfully retrieved processed results from s3 bucket')

    def remove_processed_results(self):
        print('All processed results successfully removed from s3 bucket')

class SQSStorage(StorageService):
    def get_processed_results(self):
        print('Retrieved processed results from SQS queue')

    def remove_processed_results(self):
        print('Removed processed results from SQS Queue')

class Lft:
    def __init__(self, storageService):
        self.storageService = storageService

    def process_results(self):
        self.storageService.get_processed_results()


lft = Lft(s3Storage())
lft.process_results()

sqs = Lft(SQSStorage())
sqs.process_results()