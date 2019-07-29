# coding: utf-8

"""
    Zuora API Reference

      # Introduction Welcome to the reference for the Zuora REST API!  <a href=\"http://en.wikipedia.org/wiki/REST_API\" target=\"_blank\">REST</a> is a web-service protocol that lends itself to rapid development by using everyday HTTP and JSON technology.  The Zuora REST API provides a broad set of operations and resources that:    * Enable Web Storefront integration from your website.   * Support self-service subscriber sign-ups and account management.   * Process revenue schedules through custom revenue rule models.   * Enable manipulation of most objects in the Zuora Object Model.  Want to share your opinion on how our API works for you? <a href=\"https://community.zuora.com/t5/Developers/API-Feedback-Form/gpm-p/21399\" target=\"_blank\">Tell us how you feel </a>about using our API and what we can do to make it better.  ## Access to the API  If you have a Zuora tenant, you can access the Zuora REST API via one of the following endpoints:  | Tenant              | Base URL for REST Endpoints | |-------------------------|-------------------------| |US Production | https://rest.zuora.com   | |US API Sandbox    | https://rest.apisandbox.zuora.com| |US Performance Test | https://rest.pt1.zuora.com | |EU Production | https://rest.eu.zuora.com | |EU Sandbox | https://rest.sandbox.eu.zuora.com |  The Production endpoint provides access to your live user data. API Sandbox tenants are a good place to test code without affecting real-world data. If you would like Zuora to provision an API Sandbox tenant for you, contact your Zuora representative for assistance.  **Note:** If you have a tenant in the Production Copy Environment, submit a request at <a href=\"http://support.zuora.com/\" target=\"_blank\">Zuora Global Support</a> to enable the Zuora REST API in your tenant and obtain the base URL for REST endpoints.  If you do not have a Zuora tenant, go to <a href=\"https://www.zuora.com/resource/zuora-test-drive\" target=\"_blank\">https://www.zuora.com/resource/zuora-test-drive</a> and sign up for a Production Test Drive tenant. The tenant comes with seed data, including a sample product catalog.  # API Changelog You can find the <a href=\"https://community.zuora.com/t5/Developers/API-Changelog/gpm-p/18092\" target=\"_blank\">Changelog</a> of the API Reference in the Zuora Community.  # Authentication  ## OAuth v2.0  Zuora recommends that you use OAuth v2.0 to authenticate to the Zuora REST API. Currently, OAuth is not available in every environment. See [Zuora Testing Environments](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/D_Zuora_Environments) for more information.  Zuora recommends you to create a dedicated API user with API write access on a tenant when authenticating via OAuth, and then create an OAuth client for this user. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for how to do this. By creating a dedicated API user, you can control permissions of the API user without affecting other non-API users.  If a user is deactivated, all of the user's OAuth clients will be automatically deactivated.  Authenticating via OAuth requires the following steps: 1. Create a Client 2. Generate a Token 3. Make Authenticated Requests  ### Create a Client  You must first [create an OAuth client](https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users#Create_an_OAuth_Client_for_a_User) in the Zuora UI. To do this, you must be an administrator of your Zuora tenant. This is a one-time operation. You will be provided with a Client ID and a Client Secret. Please note this information down, as it will be required for the next step.  **Note:** The OAuth client will be owned by a Zuora user account. If you want to perform PUT, POST, or DELETE operations using the OAuth client, the owner of the OAuth client must have a Platform role that includes the \"API Write Access\" permission.  ### Generate a Token  After creating a client, you must make a call to obtain a bearer token using the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) operation. This operation requires the following parameters: - `client_id` - the Client ID displayed when you created the OAuth client in the previous step - `client_secret` - the Client Secret displayed when you created the OAuth client in the previous step - `grant_type` - must be set to `client_credentials`  **Note**: The Client ID and Client Secret mentioned above were displayed when you created the OAuth Client in the prior step. The [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response specifies how long the bearer token is valid for. Call [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) again to generate a new bearer token.  ### Make Authenticated Requests  To authenticate subsequent API requests, you must provide a valid bearer token in an HTTP header:  `Authorization: Bearer {bearer_token}`  If you have [Zuora Multi-entity](https://www.zuora.com/developer/api-reference/#tag/Entities) enabled, you need to set an additional header to specify the ID of the entity that you want to access. You can use the `scope` field in the [Generate an OAuth token](https://www.zuora.com/developer/api-reference/#operation/createToken) response to determine whether you need to specify an entity ID.  If the `scope` field contains more than one entity ID, you must specify the ID of the entity that you want to access. For example, if the `scope` field contains `entity.1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` and `entity.c92ed977-510c-4c48-9b51-8d5e848671e9`, specify one of the following headers: - `Zuora-Entity-Ids: 1a2b7a37-3e7d-4cb3-b0e2-883de9e766cc` - `Zuora-Entity-Ids: c92ed977-510c-4c48-9b51-8d5e848671e9`  **Note**: For a limited period of time, Zuora will accept the `entityId` header as an alternative to the `Zuora-Entity-Ids` header. If you choose to set the `entityId` header, you must remove all \"-\" characters from the entity ID in the `scope` field.  If the `scope` field contains a single entity ID, you do not need to specify an entity ID.  ## Other Supported Authentication Schemes  Zuora continues to support the following additional legacy means of authentication:    * Use username and password. Include authentication with each request in the header:         * `apiAccessKeyId`      * `apiSecretAccessKey`          Zuora recommends that you create an API user specifically for making API calls. See <a href=\"https://knowledgecenter.zuora.com/CF_Users_and_Administrators/A_Administrator_Settings/Manage_Users/Create_an_API_User\" target=\"_blank\">Create an API User</a> for more information.      * Use an authorization cookie. The cookie authorizes the user to make calls to the REST API for the duration specified in  **Administration > Security Policies > Session timeout**. The cookie expiration time is reset with this duration after every call to the REST API. To obtain a cookie, call the [Connections](https://www.zuora.com/developer/api-reference/#tag/Connections) resource with the following API user information:         *   ID         *   Password        * For CORS-enabled APIs only: Include a 'single-use' token in the request header, which re-authenticates the user with each request. See below for more details.  ### Entity Id and Entity Name  The `entityId` and `entityName` parameters are only used for [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity \"Zuora Multi-entity\"). These are the legacy parameters that Zuora will only continue to support for a period of time. Zuora recommends you to use the `Zuora-Entity-Ids` parameter instead.   The  `entityId` and `entityName` parameters specify the Id and the [name of the entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/B_Introduction_to_Entity_and_Entity_Hierarchy#Name_and_Display_Name \"Introduction to Entity and Entity Hierarchy\") that you want to access, respectively. Note that you must have permission to access the entity.   You can specify either the `entityId` or `entityName` parameter in the authentication to access and view an entity.    * If both `entityId` and `entityName` are specified in the authentication, an error occurs.    * If neither `entityId` nor `entityName` is specified in the authentication, you will log in to the entity in which your user account is created.      To get the entity Id and entity name, you can use the GET Entities REST call. For more information, see [API User Authentication](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity/A_Overview_of_Multi-entity#API_User_Authentication \"API User Authentication\").      ### Token Authentication for CORS-Enabled APIs      The CORS mechanism enables REST API calls to Zuora to be made directly from your customer's browser, with all credit card and security information transmitted directly to Zuora. This minimizes your PCI compliance burden, allows you to implement advanced validation on your payment forms, and  makes your payment forms look just like any other part of your website.    For security reasons, instead of using cookies, an API request via CORS uses **tokens** for authentication.  The token method of authentication is only designed for use with requests that must originate from your customer's browser; **it should  not be considered a replacement to the existing cookie authentication** mechanism.  See [Zuora CORS REST](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Zuora_CORS_REST \"Zuora CORS REST\") for details on how CORS works and how you can begin to implement customer calls to the Zuora REST APIs. See  [HMAC Signatures](https://www.zuora.com/developer/api-reference/#operation/POSTHMACSignature \"HMAC Signatures\") for details on the HMAC method that returns the authentication token.  # Requests and Responses  ## Request IDs  As a general rule, when asked to supply a \"key\" for an account or subscription (accountKey, account-key, subscriptionKey, subscription-key), you can provide either the actual ID or  the number of the entity.  ## HTTP Request Body  Most of the parameters and data accompanying your requests will be contained in the body of the HTTP request.   The Zuora REST API accepts JSON in the HTTP request body. No other data format (e.g., XML) is supported.  ### Data Type  ([Actions](https://www.zuora.com/developer/api-reference/#tag/Actions) and CRUD operations only) We recommend that you do not specify the decimal values with quotation marks, commas, and spaces. Use characters of `+-0-9.eE`, for example, `5`, `1.9`, `-8.469`, and `7.7e2`. Also, Zuora does not convert currencies for decimal values.  ## Testing a Request  Use a third party client, such as [curl](https://curl.haxx.se \"curl\"), [Postman](https://www.getpostman.com \"Postman\"), or [Advanced REST Client](https://advancedrestclient.com \"Advanced REST Client\"), to test the Zuora REST API.  You can test the Zuora REST API from the Zuora API Sandbox or Production tenants. If connecting to Production, bear in mind that you are working with your live production data, not sample data or test data.  ## Testing with Credit Cards  Sooner or later it will probably be necessary to test some transactions that involve credit cards. For suggestions on how to handle this, see [Going Live With Your Payment Gateway](https://knowledgecenter.zuora.com/CB_Billing/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards \"C_Zuora_User_Guides/A_Billing_and_Payments/M_Payment_Gateways/C_Managing_Payment_Gateways/B_Going_Live_Payment_Gateways#Testing_with_Credit_Cards\" ).  ## Concurrent Request Limits  Zuora enforces tenant-level concurrent request limits. See <a href=\"https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Policies/Concurrent_Request_Limits\" target=\"_blank\">Concurrent Request Limits</a> for more information.  ## Timeout Limit  If a request does not complete within 120 seconds, the request times out and Zuora returns a Gateway Timeout error.  ## Error Handling  Responses and error codes are detailed in [Responses and errors](https://knowledgecenter.zuora.com/DC_Developers/C_REST_API/Responses_and_Errors \"Responses and errors\").  # Pagination  When retrieving information (using GET methods), the optional `pageSize` query parameter sets the maximum number of rows to return in a response. The maximum is `40`; larger values are treated as `40`. If this value is empty or invalid, `pageSize` typically defaults to `10`.  The default value for the maximum number of rows retrieved can be overridden at the method level.  If more rows are available, the response will include a `nextPage` element, which contains a URL for requesting the next page.  If this value is not provided, no more rows are available. No \"previous page\" element is explicitly provided; to support backward paging, use the previous call.  ## Array Size  For data items that are not paginated, the REST API supports arrays of up to 300 rows.  Thus, for instance, repeated pagination can retrieve thousands of customer accounts, but within any account an array of no more than 300 rate plans is returned.  # API Versions  The Zuora REST API are version controlled. Versioning ensures that Zuora REST API changes are backward compatible. Zuora uses a major and minor version nomenclature to manage changes. By specifying a version in a REST request, you can get expected responses regardless of future changes to the API.  ## Major Version  The major version number of the REST API appears in the REST URL. Currently, Zuora only supports the **v1** major version. For example, `POST https://rest.zuora.com/v1/subscriptions`.  ## Minor Version  Zuora uses minor versions for the REST API to control small changes. For example, a field in a REST method is deprecated and a new field is used to replace it.   Some fields in the REST methods are supported as of minor versions. If a field is not noted with a minor version, this field is available for all minor versions. If a field is noted with a minor version, this field is in version control. You must specify the supported minor version in the request header to process without an error.   If a field is in version control, it is either with a minimum minor version or a maximum minor version, or both of them. You can only use this field with the minor version between the minimum and the maximum minor versions. For example, the `invoiceCollect` field in the POST Subscription method is in version control and its maximum minor version is 189.0. You can only use this field with the minor version 189.0 or earlier.  If you specify a version number in the request header that is not supported, Zuora will use the minimum minor version of the REST API. In our REST API documentation, if a field or feature requires a minor version number, we note that in the field description.  You only need to specify the version number when you use the fields require a minor version. To specify the minor version, set the `zuora-version` parameter to the minor version number in the request header for the request call. For example, the `collect` field is in 196.0 minor version. If you want to use this field for the POST Subscription method, set the  `zuora-version` parameter to `196.0` in the request header. The `zuora-version` parameter is case sensitive.  For all the REST API fields, by default, if the minor version is not specified in the request header, Zuora will use the minimum minor version of the REST API to avoid breaking your integration.   ### Minor Version History  The supported minor versions are not serial. This section documents the changes made to each Zuora REST API minor version.  The following table lists the supported versions and the fields that have a Zuora REST API minor version.  | Fields         | Minor Version      | REST Methods    | Description | |:--------|:--------|:--------|:--------| | invoiceCollect | 189.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice and collects a payment for a subscription. | | collect        | 196.0 and later    | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Collects an automatic payment for a subscription. | | invoice | 196.0 and 207.0| [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice for a subscription. | | invoiceTargetDate | 196.0 and earlier  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | invoiceTargetDate | 207.0 and earlier  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 207.0 and later | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") |Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | targetDate | 211.0 and later | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Date through which charges are calculated on the invoice, as `yyyy-mm-dd`. | | includeExisting DraftInvoiceItems | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | includeExisting DraftDocItems | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | Specifies whether to include draft invoice items in subscription previews. Specify it to be `true` (default) to include draft invoice items in the preview result. Specify it to be `false` to excludes draft invoice items in the preview result. | | previewType | 196.0 and earlier| [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `InvoiceItem`(default), `ChargeMetrics`, and `InvoiceItemChargeMetrics`. | | previewType | 207.0 and later  | [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") | The type of preview you will receive. The possible values are `LegalDoc`(default), `ChargeMetrics`, and `LegalDocChargeMetrics`. | | runBilling  | 211.0 and later  | [Create Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_Subscription \"Create Subscription\"); [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\"); [Renew Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_RenewSubscription \"Renew Subscription\"); [Cancel Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_CancelSubscription \"Cancel Subscription\"); [Suspend Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_SuspendSubscription \"Suspend Subscription\"); [Resume Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_ResumeSubscription \"Resume Subscription\"); [Create Account](https://www.zuora.com/developer/api-reference/#operation/POST_Account \"Create Account\")|Generates an invoice or credit memo for a subscription. **Note:** Credit memos are only available if you have the Invoice Settlement feature enabled. | | invoiceDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice being generated, as `yyyy-mm-dd`. | | invoiceTargetDate | 214.0 and earlier  | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice is generated, as `yyyy-mm-dd`. | | documentDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date that should appear on the invoice and credit memo being generated, as `yyyy-mm-dd`. | | targetDate | 215.0 and later | [Invoice and Collect](https://www.zuora.com/developer/api-reference/#operation/POST_TransactionInvoicePayment \"Invoice and Collect\") |Date through which to calculate charges on this account if an invoice or a credit memo is generated, as `yyyy-mm-dd`. | | memoItemAmount | 223.0 and earlier | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | amount | 224.0 and later | [Create credit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_CreditMemoFromPrpc \"Create credit memo from charge\"); [Create debit memo from charge](https://www.zuora.com/developer/api-reference/#operation/POST_DebitMemoFromPrpc \"Create debit memo from charge\") | Amount of the memo item. | | subscriptionNumbers | 222.4 and earlier | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers of the subscriptions in an order. | | subscriptions | 223.0 and later | [Create order](https://www.zuora.com/developer/api-reference/#operation/POST_Order \"Create order\") | Container for the subscription numbers and statuses in an order. | | creditTaxItems | 238.0 and earlier | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\") | Container for the taxation items of the credit memo item. | | taxItems | 238.0 and earlier | [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the debit memo item. | | taxationItems | 239.0 and later | [Get credit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItems \"Get credit memo items\"); [Get credit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_CreditMemoItem \"Get credit memo item\"); [Get debit memo items](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItems \"Get debit memo items\"); [Get debit memo item](https://www.zuora.com/developer/api-reference/#operation/GET_DebitMemoItem \"Get debit memo item\") | Container for the taxation items of the memo item. |   #### Version 207.0 and Later  The response structure of the [Preview Subscription](https://www.zuora.com/developer/api-reference/#operation/POST_SubscriptionPreview \"Preview Subscription\") and [Update Subscription](https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription \"Update Subscription\") methods are changed. The following invoice related response fields are moved to the invoice container:    * amount   * amountWithoutTax   * taxAmount   * invoiceItems   * targetDate   * chargeMetrics  # Zuora Object Model  The following diagram presents a high-level view of the key Zuora objects. Click the image to open it in a new tab to resize it.  <a href=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" target=\"_blank\"><img src=\"https://www.zuora.com/wp-content/uploads/2017/01/ZuoraERD.jpeg\" alt=\"Zuora Object Model Diagram\"></a>  See the following articles for information about other parts of the Zuora business object model:    * <a href=\"https://knowledgecenter.zuora.com/CB_Billing/Invoice_Settlement/D_Invoice_Settlement_Object_Model\" target=\"_blank\">Invoice Settlement Object Model</a>   * <a href=\"https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/BA_Orders_Object_Model\" target=\"_blank\">Orders Object Model</a>  You can use the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation to list the fields of each Zuora object that is available in your tenant. When you call the operation, you must specify the API name of the Zuora object.  The following table provides the API name of each Zuora object:  | Object                                        | API Name                                   | |-----------------------------------------------|--------------------------------------------| | Account                                       | `Account`                                  | | Accounting Code                               | `AccountingCode`                           | | Accounting Period                             | `AccountingPeriod`                         | | Amendment                                     | `Amendment`                                | | Application Group                             | `ApplicationGroup`                         | | Billing Run                                   | <p>`BillingRun`</p><p>**Note:** The API name of this object is `BillingRun` in the [Describe object](https://www.zuora.com/developer/api-reference/#operation/GET_Describe) operation, Export ZOQL queries, and Data Query. Otherwise, the API name of this object is `BillRun`.</p> | | Contact                                       | `Contact`                                  | | Contact Snapshot                              | `ContactSnapshot`                          | | Credit Balance Adjustment                     | `CreditBalanceAdjustment`                  | | Credit Memo                                   | `CreditMemo`                               | | Credit Memo Application                       | `CreditMemoApplication`                    | | Credit Memo Application Item                  | `CreditMemoApplicationItem`                | | Credit Memo Item                              | `CreditMemoItem`                           | | Credit Memo Part                              | `CreditMemoPart`                           | | Credit Memo Part Item                         | `CreditMemoPartItem`                       | | Credit Taxation Item                          | `CreditTaxationItem`                       | | Custom Exchange Rate                          | `FXCustomRate`                             | | Debit Memo                                    | `DebitMemo`                                | | Debit Memo Item                               | `DebitMemoItem`                            | | Debit Taxation Item                           | `DebitTaxationItem`                        | | Discount Applied Metrics                      | `DiscountAppliedMetrics`                   | | Entity                                        | `Tenant`                                   | | Feature                                       | `Feature`                                  | | Gateway Reconciliation Event                  | `PaymentGatewayReconciliationEventLog`     | | Gateway Reconciliation Job                    | `PaymentReconciliationJob`                 | | Gateway Reconciliation Log                    | `PaymentReconciliationLog`                 | | Invoice                                       | `Invoice`                                  | | Invoice Adjustment                            | `InvoiceAdjustment`                        | | Invoice Item                                  | `InvoiceItem`                              | | Invoice Item Adjustment                       | `InvoiceItemAdjustment`                    | | Invoice Payment                               | `InvoicePayment`                           | | Journal Entry                                 | `JournalEntry`                             | | Journal Entry Item                            | `JournalEntryItem`                         | | Journal Run                                   | `JournalRun`                               | | Order                                         | `Order`                                    | | Order Action                                  | `OrderAction`                              | | Order ELP                                     | `OrderElp`                                 | | Order Item                                    | `OrderItem`                                | | Order MRR                                     | `OrderMrr`                                 | | Order Quantity                                | `OrderQuantity`                            | | Order TCB                                     | `OrderTcb`                                 | | Order TCV                                     | `OrderTcv`                                 | | Payment                                       | `Payment`                                  | | Payment Application                           | `PaymentApplication`                       | | Payment Application Item                      | `PaymentApplicationItem`                   | | Payment Method                                | `PaymentMethod`                            | | Payment Method Snapshot                       | `PaymentMethodSnapshot`                    | | Payment Method Transaction Log                | `PaymentMethodTransactionLog`              | | Payment Method Update                         | `UpdaterDetail`                            | | Payment Part                                  | `PaymentPart`                              | | Payment Part Item                             | `PaymentPartItem`                          | | Payment Run                                   | `PaymentRun`                               | | Payment Transaction Log                       | `PaymentTransactionLog`                    | | Processed Usage                               | `ProcessedUsage`                           | | Product                                       | `Product`                                  | | Product Feature                               | `ProductFeature`                           | | Product Rate Plan                             | `ProductRatePlan`                          | | Product Rate Plan Charge                      | `ProductRatePlanCharge`                    | | Product Rate Plan Charge Tier                 | `ProductRatePlanChargeTier`                | | Rate Plan                                     | `RatePlan`                                 | | Rate Plan Charge                              | `RatePlanCharge`                           | | Rate Plan Charge Tier                         | `RatePlanChargeTier`                       | | Refund                                        | `Refund`                                   | | Refund Application                            | `RefundApplication`                        | | Refund Application Item                       | `RefundApplicationItem`                    | | Refund Invoice Payment                        | `RefundInvoicePayment`                     | | Refund Part                                   | `RefundPart`                               | | Refund Part Item                              | `RefundPartItem`                           | | Refund Transaction Log                        | `RefundTransactionLog`                     | | Revenue Charge Summary                        | `RevenueChargeSummary`                     | | Revenue Charge Summary Item                   | `RevenueChargeSummaryItem`                 | | Revenue Event                                 | `RevenueEvent`                             | | Revenue Event Credit Memo Item                | `RevenueEventCreditMemoItem`               | | Revenue Event Debit Memo Item                 | `RevenueEventDebitMemoItem`                | | Revenue Event Invoice Item                    | `RevenueEventInvoiceItem`                  | | Revenue Event Invoice Item Adjustment         | `RevenueEventInvoiceItemAdjustment`        | | Revenue Event Item                            | `RevenueEventItem`                         | | Revenue Event Item Credit Memo Item           | `RevenueEventItemCreditMemoItem`           | | Revenue Event Item Debit Memo Item            | `RevenueEventItemDebitMemoItem`            | | Revenue Event Item Invoice Item               | `RevenueEventItemInvoiceItem`              | | Revenue Event Item Invoice Item Adjustment    | `RevenueEventItemInvoiceItemAdjustment`    | | Revenue Event Type                            | `RevenueEventType`                         | | Revenue Schedule                              | `RevenueSchedule`                          | | Revenue Schedule Credit Memo Item             | `RevenueScheduleCreditMemoItem`            | | Revenue Schedule Debit Memo Item              | `RevenueScheduleDebitMemoItem`             | | Revenue Schedule Invoice Item                 | `RevenueScheduleInvoiceItem`               | | Revenue Schedule Invoice Item Adjustment      | `RevenueScheduleInvoiceItemAdjustment`     | | Revenue Schedule Item                         | `RevenueScheduleItem`                      | | Revenue Schedule Item Credit Memo Item        | `RevenueScheduleItemCreditMemoItem`        | | Revenue Schedule Item Debit Memo Item         | `RevenueScheduleItemDebitMemoItem`         | | Revenue Schedule Item Invoice Item            | `RevenueScheduleItemInvoiceItem`           | | Revenue Schedule Item Invoice Item Adjustment | `RevenueScheduleItemInvoiceItemAdjustment` | | Subscription                                  | `Subscription`                             | | Subscription Product Feature                  | `SubscriptionProductFeature`               | | Taxable Item Snapshot                         | `TaxableItemSnapshot`                      | | Taxation Item                                 | `TaxationItem`                             | | Updater Batch                                 | `UpdaterBatch`                             | | Usage                                         | `Usage`                                    |   # noqa: E501

    OpenAPI spec version: 2019-07-26
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class POSTRejectPaymentResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'amount': 'float',
        'cancelled_on': 'datetime',
        'comment': 'str',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'credit_memo_id': 'str',
        'finance_information': 'object',
        'gateway_id': 'str',
        'gateway_response': 'str',
        'gateway_response_code': 'str',
        'gateway_state': 'str',
        'id': 'str',
        'marked_for_submission_on': 'datetime',
        'method_type': 'str',
        'number': 'str',
        'payment_id': 'str',
        'payment_method_id': 'str',
        'payment_method_snapshot_id': 'str',
        'reason_code': 'str',
        'reference_id': 'str',
        'refund_date': 'date',
        'refund_transaction_time': 'datetime',
        'second_refund_reference_id': 'str',
        'settled_on': 'datetime',
        'soft_descriptor': 'str',
        'soft_descriptor_phone': 'str',
        'status': 'str',
        'submitted_on': 'datetime',
        'success': 'bool',
        'type': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'account_id': 'accountId',
        'amount': 'amount',
        'cancelled_on': 'cancelledOn',
        'comment': 'comment',
        'created_by_id': 'createdById',
        'created_date': 'createdDate',
        'credit_memo_id': 'creditMemoId',
        'finance_information': 'financeInformation',
        'gateway_id': 'gatewayId',
        'gateway_response': 'gatewayResponse',
        'gateway_response_code': 'gatewayResponseCode',
        'gateway_state': 'gatewayState',
        'id': 'id',
        'marked_for_submission_on': 'markedForSubmissionOn',
        'method_type': 'methodType',
        'number': 'number',
        'payment_id': 'paymentId',
        'payment_method_id': 'paymentMethodId',
        'payment_method_snapshot_id': 'paymentMethodSnapshotId',
        'reason_code': 'reasonCode',
        'reference_id': 'referenceId',
        'refund_date': 'refundDate',
        'refund_transaction_time': 'refundTransactionTime',
        'second_refund_reference_id': 'secondRefundReferenceId',
        'settled_on': 'settledOn',
        'soft_descriptor': 'softDescriptor',
        'soft_descriptor_phone': 'softDescriptorPhone',
        'status': 'status',
        'submitted_on': 'submittedOn',
        'success': 'success',
        'type': 'type',
        'updated_by_id': 'updatedById',
        'updated_date': 'updatedDate'
    }

    def __init__(self, account_id=None, amount=None, cancelled_on=None, comment=None, created_by_id=None, created_date=None, credit_memo_id=None, finance_information=None, gateway_id=None, gateway_response=None, gateway_response_code=None, gateway_state=None, id=None, marked_for_submission_on=None, method_type=None, number=None, payment_id=None, payment_method_id=None, payment_method_snapshot_id=None, reason_code=None, reference_id=None, refund_date=None, refund_transaction_time=None, second_refund_reference_id=None, settled_on=None, soft_descriptor=None, soft_descriptor_phone=None, status=None, submitted_on=None, success=None, type=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """POSTRejectPaymentResponse - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._amount = None
        self._cancelled_on = None
        self._comment = None
        self._created_by_id = None
        self._created_date = None
        self._credit_memo_id = None
        self._finance_information = None
        self._gateway_id = None
        self._gateway_response = None
        self._gateway_response_code = None
        self._gateway_state = None
        self._id = None
        self._marked_for_submission_on = None
        self._method_type = None
        self._number = None
        self._payment_id = None
        self._payment_method_id = None
        self._payment_method_snapshot_id = None
        self._reason_code = None
        self._reference_id = None
        self._refund_date = None
        self._refund_transaction_time = None
        self._second_refund_reference_id = None
        self._settled_on = None
        self._soft_descriptor = None
        self._soft_descriptor_phone = None
        self._status = None
        self._submitted_on = None
        self._success = None
        self._type = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if cancelled_on is not None:
            self.cancelled_on = cancelled_on
        if comment is not None:
            self.comment = comment
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if credit_memo_id is not None:
            self.credit_memo_id = credit_memo_id
        if finance_information is not None:
            self.finance_information = finance_information
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if gateway_response is not None:
            self.gateway_response = gateway_response
        if gateway_response_code is not None:
            self.gateway_response_code = gateway_response_code
        if gateway_state is not None:
            self.gateway_state = gateway_state
        if id is not None:
            self.id = id
        if marked_for_submission_on is not None:
            self.marked_for_submission_on = marked_for_submission_on
        if method_type is not None:
            self.method_type = method_type
        if number is not None:
            self.number = number
        if payment_id is not None:
            self.payment_id = payment_id
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if payment_method_snapshot_id is not None:
            self.payment_method_snapshot_id = payment_method_snapshot_id
        if reason_code is not None:
            self.reason_code = reason_code
        if reference_id is not None:
            self.reference_id = reference_id
        if refund_date is not None:
            self.refund_date = refund_date
        if refund_transaction_time is not None:
            self.refund_transaction_time = refund_transaction_time
        if second_refund_reference_id is not None:
            self.second_refund_reference_id = second_refund_reference_id
        if settled_on is not None:
            self.settled_on = settled_on
        if soft_descriptor is not None:
            self.soft_descriptor = soft_descriptor
        if soft_descriptor_phone is not None:
            self.soft_descriptor_phone = soft_descriptor_phone
        if status is not None:
            self.status = status
        if submitted_on is not None:
            self.submitted_on = submitted_on
        if success is not None:
            self.success = success
        if type is not None:
            self.type = type
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def account_id(self):
        """Gets the account_id of this POSTRejectPaymentResponse.  # noqa: E501

        The ID of the customer account that the payment is for.   # noqa: E501

        :return: The account_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this POSTRejectPaymentResponse.

        The ID of the customer account that the payment is for.   # noqa: E501

        :param account_id: The account_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this POSTRejectPaymentResponse.  # noqa: E501

        The total amount of the payment.   # noqa: E501

        :return: The amount of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this POSTRejectPaymentResponse.

        The total amount of the payment.   # noqa: E501

        :param amount: The amount of this POSTRejectPaymentResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def cancelled_on(self):
        """Gets the cancelled_on of this POSTRejectPaymentResponse.  # noqa: E501

        The date and time when the payment was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The cancelled_on of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._cancelled_on

    @cancelled_on.setter
    def cancelled_on(self, cancelled_on):
        """Sets the cancelled_on of this POSTRejectPaymentResponse.

        The date and time when the payment was cancelled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param cancelled_on: The cancelled_on of this POSTRejectPaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._cancelled_on = cancelled_on

    @property
    def comment(self):
        """Gets the comment of this POSTRejectPaymentResponse.  # noqa: E501

        Comments about the payment.   # noqa: E501

        :return: The comment of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this POSTRejectPaymentResponse.

        Comments about the payment.   # noqa: E501

        :param comment: The comment of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def created_by_id(self):
        """Gets the created_by_id of this POSTRejectPaymentResponse.  # noqa: E501

        The ID of the Zuora user who created the refund.   # noqa: E501

        :return: The created_by_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this POSTRejectPaymentResponse.

        The ID of the Zuora user who created the refund.   # noqa: E501

        :param created_by_id: The created_by_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this POSTRejectPaymentResponse.  # noqa: E501

        The date and time when the chargeback is created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2019-03-01 15:31:10.   # noqa: E501

        :return: The created_date of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this POSTRejectPaymentResponse.

        The date and time when the chargeback is created, in `yyyy-mm-dd hh:mm:ss` format. For example, 2019-03-01 15:31:10.   # noqa: E501

        :param created_date: The created_date of this POSTRejectPaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def credit_memo_id(self):
        """Gets the credit_memo_id of this POSTRejectPaymentResponse.  # noqa: E501

        The ID of the credit memo that is refunded.   # noqa: E501

        :return: The credit_memo_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._credit_memo_id

    @credit_memo_id.setter
    def credit_memo_id(self, credit_memo_id):
        """Sets the credit_memo_id of this POSTRejectPaymentResponse.

        The ID of the credit memo that is refunded.   # noqa: E501

        :param credit_memo_id: The credit_memo_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._credit_memo_id = credit_memo_id

    @property
    def finance_information(self):
        """Gets the finance_information of this POSTRejectPaymentResponse.  # noqa: E501

        Container for the finance information related to the refund.   # noqa: E501

        :return: The finance_information of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: object
        """
        return self._finance_information

    @finance_information.setter
    def finance_information(self, finance_information):
        """Sets the finance_information of this POSTRejectPaymentResponse.

        Container for the finance information related to the refund.   # noqa: E501

        :param finance_information: The finance_information of this POSTRejectPaymentResponse.  # noqa: E501
        :type: object
        """

        self._finance_information = finance_information

    @property
    def gateway_id(self):
        """Gets the gateway_id of this POSTRejectPaymentResponse.  # noqa: E501

        The ID of the gateway instance that processes the payment.   # noqa: E501

        :return: The gateway_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this POSTRejectPaymentResponse.

        The ID of the gateway instance that processes the payment.   # noqa: E501

        :param gateway_id: The gateway_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._gateway_id = gateway_id

    @property
    def gateway_response(self):
        """Gets the gateway_response of this POSTRejectPaymentResponse.  # noqa: E501

        The message returned from the payment gateway for the payment. This message is gateway-dependent.   # noqa: E501

        :return: The gateway_response of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._gateway_response

    @gateway_response.setter
    def gateway_response(self, gateway_response):
        """Sets the gateway_response of this POSTRejectPaymentResponse.

        The message returned from the payment gateway for the payment. This message is gateway-dependent.   # noqa: E501

        :param gateway_response: The gateway_response of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._gateway_response = gateway_response

    @property
    def gateway_response_code(self):
        """Gets the gateway_response_code of this POSTRejectPaymentResponse.  # noqa: E501

        The code returned from the payment gateway for the payment. This code is gateway-dependent.   # noqa: E501

        :return: The gateway_response_code of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._gateway_response_code

    @gateway_response_code.setter
    def gateway_response_code(self, gateway_response_code):
        """Sets the gateway_response_code of this POSTRejectPaymentResponse.

        The code returned from the payment gateway for the payment. This code is gateway-dependent.   # noqa: E501

        :param gateway_response_code: The gateway_response_code of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._gateway_response_code = gateway_response_code

    @property
    def gateway_state(self):
        """Gets the gateway_state of this POSTRejectPaymentResponse.  # noqa: E501

        The status of the payment in the gateway; used for reconciliation.   # noqa: E501

        :return: The gateway_state of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._gateway_state

    @gateway_state.setter
    def gateway_state(self, gateway_state):
        """Sets the gateway_state of this POSTRejectPaymentResponse.

        The status of the payment in the gateway; used for reconciliation.   # noqa: E501

        :param gateway_state: The gateway_state of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["MarkedForSubmission", "Submitted", "Settled", "NotSubmitted", "FailedToSettle"]  # noqa: E501
        if gateway_state not in allowed_values:
            raise ValueError(
                "Invalid value for `gateway_state` ({0}), must be one of {1}"  # noqa: E501
                .format(gateway_state, allowed_values)
            )

        self._gateway_state = gateway_state

    @property
    def id(self):
        """Gets the id of this POSTRejectPaymentResponse.  # noqa: E501

        The ID of the payment chargeback.   # noqa: E501

        :return: The id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this POSTRejectPaymentResponse.

        The ID of the payment chargeback.   # noqa: E501

        :param id: The id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def marked_for_submission_on(self):
        """Gets the marked_for_submission_on of this POSTRejectPaymentResponse.  # noqa: E501

        The date and time when a charge was marked and waiting for batch submission to the payment process, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The marked_for_submission_on of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._marked_for_submission_on

    @marked_for_submission_on.setter
    def marked_for_submission_on(self, marked_for_submission_on):
        """Sets the marked_for_submission_on of this POSTRejectPaymentResponse.

        The date and time when a charge was marked and waiting for batch submission to the payment process, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param marked_for_submission_on: The marked_for_submission_on of this POSTRejectPaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._marked_for_submission_on = marked_for_submission_on

    @property
    def method_type(self):
        """Gets the method_type of this POSTRejectPaymentResponse.  # noqa: E501

        How an external refund was issued to a customer.    # noqa: E501

        :return: The method_type of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._method_type

    @method_type.setter
    def method_type(self, method_type):
        """Sets the method_type of this POSTRejectPaymentResponse.

        How an external refund was issued to a customer.    # noqa: E501

        :param method_type: The method_type of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACH", "Cash", "Check", "CreditCard", "PayPal", "WireTransfer", "DebitCard", "CreditCardReferenceTransaction", "BankTransfer", "Other"]  # noqa: E501
        if method_type not in allowed_values:
            raise ValueError(
                "Invalid value for `method_type` ({0}), must be one of {1}"  # noqa: E501
                .format(method_type, allowed_values)
            )

        self._method_type = method_type

    @property
    def number(self):
        """Gets the number of this POSTRejectPaymentResponse.  # noqa: E501

        The unique identification number of the payment. For example, P-00000001.   # noqa: E501

        :return: The number of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this POSTRejectPaymentResponse.

        The unique identification number of the payment. For example, P-00000001.   # noqa: E501

        :param number: The number of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def payment_id(self):
        """Gets the payment_id of this POSTRejectPaymentResponse.  # noqa: E501

        The ID of the payment that is refunded.   # noqa: E501

        :return: The payment_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this POSTRejectPaymentResponse.

        The ID of the payment that is refunded.   # noqa: E501

        :param payment_id: The payment_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_id = payment_id

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this POSTRejectPaymentResponse.  # noqa: E501

        The unique ID of the payment method that the customer used to make the payment.   # noqa: E501

        :return: The payment_method_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this POSTRejectPaymentResponse.

        The unique ID of the payment method that the customer used to make the payment.   # noqa: E501

        :param payment_method_id: The payment_method_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def payment_method_snapshot_id(self):
        """Gets the payment_method_snapshot_id of this POSTRejectPaymentResponse.  # noqa: E501

        The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.   # noqa: E501

        :return: The payment_method_snapshot_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_snapshot_id

    @payment_method_snapshot_id.setter
    def payment_method_snapshot_id(self, payment_method_snapshot_id):
        """Sets the payment_method_snapshot_id of this POSTRejectPaymentResponse.

        The unique ID of the payment method snapshot which is a copy of the particular Payment Method used in a transaction.   # noqa: E501

        :param payment_method_snapshot_id: The payment_method_snapshot_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_method_snapshot_id = payment_method_snapshot_id

    @property
    def reason_code(self):
        """Gets the reason_code of this POSTRejectPaymentResponse.  # noqa: E501

        A code identifying the reason for the transaction.         # noqa: E501

        :return: The reason_code of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this POSTRejectPaymentResponse.

        A code identifying the reason for the transaction.         # noqa: E501

        :param reason_code: The reason_code of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def reference_id(self):
        """Gets the reference_id of this POSTRejectPaymentResponse.  # noqa: E501

        The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments.   # noqa: E501

        :return: The reference_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this POSTRejectPaymentResponse.

        The transaction ID returned by the payment gateway for an electronic refund. Use this field to reconcile refunds between your gateway and Zuora Payments.   # noqa: E501

        :param reference_id: The reference_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def refund_date(self):
        """Gets the refund_date of this POSTRejectPaymentResponse.  # noqa: E501

        The date when the refund takes effect, in `yyyy-mm-dd` format. For example, 2017-03-01.          # noqa: E501

        :return: The refund_date of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: date
        """
        return self._refund_date

    @refund_date.setter
    def refund_date(self, refund_date):
        """Sets the refund_date of this POSTRejectPaymentResponse.

        The date when the refund takes effect, in `yyyy-mm-dd` format. For example, 2017-03-01.          # noqa: E501

        :param refund_date: The refund_date of this POSTRejectPaymentResponse.  # noqa: E501
        :type: date
        """

        self._refund_date = refund_date

    @property
    def refund_transaction_time(self):
        """Gets the refund_transaction_time of this POSTRejectPaymentResponse.  # noqa: E501

        The date and time when the refund was issued, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The refund_transaction_time of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._refund_transaction_time

    @refund_transaction_time.setter
    def refund_transaction_time(self, refund_transaction_time):
        """Sets the refund_transaction_time of this POSTRejectPaymentResponse.

        The date and time when the refund was issued, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param refund_transaction_time: The refund_transaction_time of this POSTRejectPaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._refund_transaction_time = refund_transaction_time

    @property
    def second_refund_reference_id(self):
        """Gets the second_refund_reference_id of this POSTRejectPaymentResponse.  # noqa: E501

        The transaction ID returned by the payment gateway if there is an additional refund.    # noqa: E501

        :return: The second_refund_reference_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._second_refund_reference_id

    @second_refund_reference_id.setter
    def second_refund_reference_id(self, second_refund_reference_id):
        """Sets the second_refund_reference_id of this POSTRejectPaymentResponse.

        The transaction ID returned by the payment gateway if there is an additional refund.    # noqa: E501

        :param second_refund_reference_id: The second_refund_reference_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._second_refund_reference_id = second_refund_reference_id

    @property
    def settled_on(self):
        """Gets the settled_on of this POSTRejectPaymentResponse.  # noqa: E501

        The date and time when the transaction is settled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :return: The settled_on of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._settled_on

    @settled_on.setter
    def settled_on(self, settled_on):
        """Sets the settled_on of this POSTRejectPaymentResponse.

        The date and time when the transaction is settled, in `yyyy-mm-dd hh:mm:ss` format.   # noqa: E501

        :param settled_on: The settled_on of this POSTRejectPaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._settled_on = settled_on

    @property
    def soft_descriptor(self):
        """Gets the soft_descriptor of this POSTRejectPaymentResponse.  # noqa: E501

        A payment gateway-specific field that maps Zuora to other gateways.   # noqa: E501

        :return: The soft_descriptor of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._soft_descriptor

    @soft_descriptor.setter
    def soft_descriptor(self, soft_descriptor):
        """Sets the soft_descriptor of this POSTRejectPaymentResponse.

        A payment gateway-specific field that maps Zuora to other gateways.   # noqa: E501

        :param soft_descriptor: The soft_descriptor of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._soft_descriptor = soft_descriptor

    @property
    def soft_descriptor_phone(self):
        """Gets the soft_descriptor_phone of this POSTRejectPaymentResponse.  # noqa: E501

        A payment gateway-specific field that maps Zuora to other gateways.             # noqa: E501

        :return: The soft_descriptor_phone of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._soft_descriptor_phone

    @soft_descriptor_phone.setter
    def soft_descriptor_phone(self, soft_descriptor_phone):
        """Sets the soft_descriptor_phone of this POSTRejectPaymentResponse.

        A payment gateway-specific field that maps Zuora to other gateways.             # noqa: E501

        :param soft_descriptor_phone: The soft_descriptor_phone of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._soft_descriptor_phone = soft_descriptor_phone

    @property
    def status(self):
        """Gets the status of this POSTRejectPaymentResponse.  # noqa: E501

        The status of the payment.   # noqa: E501

        :return: The status of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this POSTRejectPaymentResponse.

        The status of the payment.   # noqa: E501

        :param status: The status of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def submitted_on(self):
        """Gets the submitted_on of this POSTRejectPaymentResponse.  # noqa: E501

        The date and time when the payment was submitted, in yyyy-mm-dd hh:mm:ss format.   # noqa: E501

        :return: The submitted_on of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_on

    @submitted_on.setter
    def submitted_on(self, submitted_on):
        """Sets the submitted_on of this POSTRejectPaymentResponse.

        The date and time when the payment was submitted, in yyyy-mm-dd hh:mm:ss format.   # noqa: E501

        :param submitted_on: The submitted_on of this POSTRejectPaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._submitted_on = submitted_on

    @property
    def success(self):
        """Gets the success of this POSTRejectPaymentResponse.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this POSTRejectPaymentResponse.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this POSTRejectPaymentResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def type(self):
        """Gets the type of this POSTRejectPaymentResponse.  # noqa: E501

        The type of the payment.   # noqa: E501

        :return: The type of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this POSTRejectPaymentResponse.

        The type of the payment.   # noqa: E501

        :param type: The type of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["External", "Electronic"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this POSTRejectPaymentResponse.  # noqa: E501

        The ID of the Zuora user who last updated the payment.   # noqa: E501

        :return: The updated_by_id of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this POSTRejectPaymentResponse.

        The ID of the Zuora user who last updated the payment.   # noqa: E501

        :param updated_by_id: The updated_by_id of this POSTRejectPaymentResponse.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this POSTRejectPaymentResponse.  # noqa: E501

        The date and time when the payment was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2019-03-02 15:36:10.   # noqa: E501

        :return: The updated_date of this POSTRejectPaymentResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this POSTRejectPaymentResponse.

        The date and time when the payment was last updated, in `yyyy-mm-dd hh:mm:ss` format. For example, 2019-03-02 15:36:10.   # noqa: E501

        :param updated_date: The updated_date of this POSTRejectPaymentResponse.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(POSTRejectPaymentResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, POSTRejectPaymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
