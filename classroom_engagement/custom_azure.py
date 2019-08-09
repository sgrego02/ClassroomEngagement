from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djangoaccountstorage1' # Must be replaced by your <storage_account_name>
    account_key = 'wjlYmo5Q0E9306csL05O0UrOZnoz2fXSC9sxRIucjN//XAgvqTWNV5y1WIYSEJBVMSwVhva59qsugBevXHs3HA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangoaccountstorage1' # Must be replaced by your storage_account_name
    account_key = 'wjlYmo5Q0E9306csL05O0UrOZnoz2fXSC9sxRIucjN//XAgvqTWNV5y1WIYSEJBVMSwVhva59qsugBevXHs3HA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None