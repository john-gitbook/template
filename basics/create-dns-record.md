# Create a DNS Record

Similar to creating a primary zone, you need to provide the UUID of the primary zone to host the new record.

{% hint style="info" %} 
**Note:** DNS records are further categorized into various record types, each with unique specifications. For more information, see [<mark style="color:blue;">FAQ<mark>](../cloud-dns-faq.md).
{% endhint %}

{% hint style="info" %} 
**Prerequisite:** You need an IONOS Cloud account with API credentials configured with the appropriate permissions.
{% endhint %}

To create a primary zone of Type A, follow this step:

1\. Perform a `POST` request with these details:
 * corresponding UUID of the primary zone
 * name of the subdomain; example: www
 * record type; in this case: A
 * content or destination of the A record in the form of an IPv4 address; example: `1.1.1.1`
 * TTL you need (minimum 60 seconds and maximum 86.400 seconds), and
 * status of the DNS record (enable), true or false.

{% hint style="success" %} 
**Result:** On a successful POST request, you receive a response with the DNS record having the UUID assigned.
{% endhint %}

{% hint style="info" %} 
**Info:** If you want to create a Wildcard DNS record, you need to provide * as the name of your DNS record to match the requests for all non-existent names under your primary zone name.
{% endhint %}


### Request

```bash
curl --location \  
<!-- markdown-link-check-disable-next-line --> 
--request POST 'https://dns.de-fra.ionos.com/zones/<zone-uuid>/records/<record-uuid>' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJraWQiO' \
--header 'Content-Type: application/json' \
--data '{
   "properties": {
    "name": "*",
    "type": "A",
    "content": "172.30.40.50,
    "ttl": 3600,
    "enabled": true
  }

}'

```


### Response

**202 Successful operation**

```json
{
  "id": "90d81ac0-3a30-44d4-95a5-12959effa6ee",
  "type": "record",
  "href": "<RESOURCE-URI>",
  "metadata": {
    "createdDate": "2022-08-21T15:52:53Z",
    "createdBy": "ionos:iam:cloud:31960002:users/87f9a82e-b28d-49ed-9d04-fba2c0459cd3",
    "createdByUserId": "87f9a82e-b28d-49ed-9d04-fba2c0459cd3",
    "lastModifiedDate": "2022-08-21T15:52:53Z",
    "lastModifiedBy": "ionos:iam:cloud:31960002:users/87f9a82e-b28d-49ed-9d04-fba2c0459cd3",
    "lastModifiedByUserId": "63cef532-26fe-4a64-a4e0-de7c8a506c90",
    "resourceURN": "ionos:<product>:<location>:<contract>:<resource-path>",
    "state": "CREATED",
    "fqdn": "*.example.com",
    "zoneId": "2a4428b3-dbe0-4357-9c02-609025b3a40f"
  },
  "properties": {
    "name": "*",
    "type": "A",
    "content": "192.0.2.2",
    "ttl": 3600,
    "enabled": true
  }
}

```

#### Response Fields

| Field                | Type   | Description                                                                 | Example                              |
|----------------------|--------|-----------------------------------------------------------------------------|--------------------------------------|
| **id**               | string | UUID of the newly created  record                                        | 90d81ac0-3a30-44d4-95a5-12959effa6ee |
| **type**             | string | Type of the resource                                                      | record                              |
  <!-- markdown-link-check-disable-next-line -->
| **href**             | string | Absolute path to the newly created DNS record                     | https://dns.de-fra.ionos.com/zones/9747ccb3-e51f-4d5c-8641-b0e8805149cc/records/aa957ef3-f29e-4ebc-ba01-a763abf02878 |
| **createdDate**      | string | Record creation timestamp           | 2022-08-21T15:52:53Z                                               |  
| **createdBy**        | string | Unique name of the identity that created the record    | ionos:iam:cloud:31960002:users/87f9a82e-b28d-49ed-9d04-fba2c0459cd3 |
| **createdByUserId**  | string | The unique ID of the user who created the record   | 87f9a82e-b28d-49ed-9d04-fba2c0459cd3                                    |
| **lastModifiedDate** | string | Record update timestamp             | 2022-08-21T15:52:53Z                                                                 |
| **lastModifiedBy**   | string | Unique name of the identity that created the record | ionos:iam:cloud:31960002:users/87f9a82e-b28d-49ed-9d04-fba2c0459cd3    |
| **lastModifiedByUserId** | string | Unique ID of the user has last modified the record  | 63cef532-26fe-4a64-a4e0-de7c8a506c90                               |
| **resourceURN** | string | Unique name of the resource             | `ionos:<product>:<location>:<contract>:<resource-path>`                                   |
| **zoneId**           | string | UUID of the primary zone of the DNS record                                      | `2a4428b3-dbe0-4357-9c02-609025b3a40f` |
| **fqdn**             | string | Fully qualified domain name resulting from the record name and the zoneName | *.example.com                        |
| **state**            | string | State of the request                                                        | CREATED                              |


## Quota

To retrieve the quota of DNS records, perform a GET request to the `/quota` endpoint.

{% hint style="success" %} 
**Result:** On a successful GET request, you receive a response containing the quota limits and quota usage for your contract.
{% endhint %}

### Request

```bash
  <!-- markdown-link-check-disable-next-line -->
curl --location 'https://dns.de-fra.ionos.com/quota' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJraWQiO' \
--header 'Content-Type: application/json'
```

### Response

**200 OK**

```json
{
  "quotaLimits": {
    "records": 100000,
    "reverseRecords": 5000,
    "secondaryZones": 100000,
    "zones": 50000
  },
  "quotaUsage": {
    "records": 9,
    "reverseRecords": 1,
    "secondaryZones": 6,
    "zones": 5
  }
}
```

#### Response Fields

| Field                | Type   | Description                                  | Example                                             |
|----------------------|--------|----------------------------------------------|-----------------------------------------------------|
| **records**          | string | Number of DNS records                        | 100000                                              |
| **reverseRecords**   | string | Number of reverse DNS records                | 5000                                                |
| **secondaryZones**   | string | Number of secondary zones                | 100000                                              |
| **zones**            | string | Number of primary zones                          | 50000                                               |
| **records**          | string | Number of DNS records used                   | 9                                                   |
| **reverseRecords**   | string | Number of reverse DNS records used           | 1                                                   |
| **secondaryZones**   | string | Number of secondary zones used           | 6                                                   |
| **zones**            | string | Number of primary zones used                     | 5                                                   |

