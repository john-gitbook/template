# August 2024

## What's new

### [<mark style="color:blue;">**Replication Enhancement**</mark>](../../../storage-&-backup/ionos-object-storage/settings/replication.md)

{% hint style="success" %}
**August 26**

IONOS Object Storage has extended support for the **Replication** feature through the DCD. You can now replicate data from user-owned buckets to contract-owned buckets in the `eu-central-3` region. Previously, this functionality was only available via the API.

{% endhint %}


### [<mark style="color:blue;">**Enable Access Logging for Application Load Balancer**</mark>](../../../network-services/application-load-balancer/how-tos/access-logging.md)


{% hint style="success" %}
**August 22**

This release introduces the **Access Logging** feature in Managed Application Load Balancer (ALB). It enhances monitoring and analyzing ALB traffic with detailed logging capabilities.


{% endhint %}

### [<mark style="color:blue;">**Enable Access Logging for Network Load Balancer**</mark>](../../../network-services/network-load-balancer/access-logging.md)


{% hint style="success" %}
**August 22**

This release introduces the **Access Logging** feature in Managed Network Load Balancer (NLB). It enhances monitoring and analyzing NLB traffic with detailed logging capabilities.

{% endhint %}

### [<mark style="color:blue;">**gRPC Support**</mark>](../../../network-services/application-load-balancer/how-tos/configure-grpc.md) and [<mark style="color:blue;">**WebSocket Support**</mark>](../../../network-services/application-load-balancer/how-tos/configure-websocket.md)
{% hint style="success" %}
**August 22**

New capabilities have been added to the Managed Application Load Balancer:

[<mark style="color:blue;">Configure gRPC Support</mark>](../../../network-services/application-load-balancer/how-tos/configure-grpc.md)

[<mark style="color:blue;">Configure WebSocket Support</mark>](../../../network-services/application-load-balancer/how-tos/configure-websocket.md)

These enhancements provide comprehensive instructions for setting up gRPC that enables users to define service methods and messages in a language-agnostic way, making it easy to create APIs that work seamlessly across different platforms and setting up WebSocket support, a communication protocol that provides full-duplex communication channels over a single TCP connection.

{% endhint %}

### [<mark style="color:blue;">**Monitoring Service**</mark>](../../../observability/monitoring-service/README.md)
{% hint style="success" %}
**August 19**

This release introduces **Monitoring Service**. IONOS Cloud introduces the Monitoring Service, which provides a centralized and scalable solution for monitoring and analyzing your application and infrastructure metrics. Hence, [<mark style="color:blue;">Monitoring as a Service</mark>](../../../observability/monitoring-as-a-service/README.md) is now considered a legacy. We recommend switching to the Monitoring Service for better support and capabilities. For more information, see [<mark style="color:blue;">FAQs</mark>](../../../observability/monitoring-service/monitoring-service-FAQs.md).

{% endhint %}

### [<mark style="color:blue;">**Private Container Registry IP ACLs**</mark>](../../../containers/private-container-registry/api-howtos/create_registry.md)

{% hint style="success" %}
**August 16**

The Private Container Registry now supports IP Access Control Lists (IP ACLs), offering enhanced security and granular access control. This feature allows you to specify IP subnets permitted to access your registry, limiting access to trusted sources within your network. IP ACLs are easy to configure via the API with the `apiSubnetAllowList` parameter. Once configured, access attempts from outside the allowed subnets are immediately blocked, ensuring real-time protection without disrupting authorized users.


{% endhint %}

### [<mark style="color:blue;">**Password Policy Manager**</mark>](../../../management/identity-access-management/password-policy-management.md)


{% hint style="success" %}
**August 14**

The new **Password Policy Manager** feature is now available for contract owners, enabling the creation of a customizable password policy that strengthens security within their contracts. Using the [<mark style="color:blue;">DCD</mark>](../../../management/identity-access-management/password-policy-management.md#password-policy-manager-in-the-dcd) or the [<mark style="color:blue;">IAM Identity Password Policies API</mark>](https://api.ionos.com/docs/identity-policy/v1/#tag/PasswordPolicy), contract owners can manage password policy. 

{% endhint %}

### [<mark style="color:blue;">**Kubernetes Version 1.27 End-of-Life**</mark>](../../../containers/managed-kubernetes/overview/managed-k8s-schedule.md)


{% hint style="success" %}
**August 14**

Kubernetes Version 1.27 has now reached its End of Life (EOL). From now on, you cannot provision any more clusters or node pools for version 1.27. Existing clusters or node pools running on version 1.27 will be automatically upgraded to version 1.28 during the next scheduled maintenance window after August 14, 2024.

{% endhint %}

### [<mark style="color:blue;">**Access Object Storage from a Private LAN**</mark>](../../../storage-&-backup/ionos-object-storage/how-tos/access-object-storage-from-private-lan.md)

{% hint style="success" %}
**August 9**

You can now set up accessing Object Storage over a private LAN by configuring a Managed Network Load Balancer (NLB) with the public IP addresses of the required Object Storage endpoint as the Target IP address and configuring the **Private IP** as the **Listener IP** of the forwarding rule. 
{% endhint %}

### [<mark style="color:blue;">**Kubernetes Version 1.27 End-of-Life Notification**</mark>](../../../containers/managed-kubernetes/overview/managed-k8s-schedule.md)

{% hint style="success" %}
**August 8**

This is to inform you that Managed Kubernetes version 1.27 will reach its end of life (EOL) on August 14, 2024. After that, you cannot create new clusters or node pools using Kubernetes version 1.27. Existing clusters or node pools running on version 1.27 will be automatically upgraded to version 1.28 during the next scheduled maintenance window after the EOL date.


{% endhint %}

### [<mark style="color:blue;">**Auto-Renewable SSL Certificate Support**</mark>](../../../security/certificate-manager/README.md)

{% hint style="success" %}
**August 2**

The Certificate Manager now supports the auto-renew of SSL certificates via the [<mark style="color:blue;">API</mark>](https://api.ionos.com/docs/certificatemanager/v2/). With this function, the certificate manager automatically renews the certificate before it expires. The renewed certificate is also available in the DCD to use them. This feature is currently supported only via the API and available on a request basis. To access this feature, please contact your sales representative or [<mark style="color:blue;">IONOS Cloud Support</mark>](https://docs.ionos.com/support/general-information/contact-information).
{% endhint %}

### [<mark style="color:blue;">**Network File Storage (NFS) Volumes for Kubernetes**</mark>](../../../containers/managed-kubernetes/how-tos/mount-an-nfs-volume.md)

{% hint style="success" %}
**August 1**

IONOS releases NFS Volumes support for Kubernetes. This feature allows the integration of IONOS Network File Storage (NFS) with Kubernetes clusters, mounting NFS volumes as PVCs in the cluster. Network File Storage is initially available only in the German data centers (Frankfurt and Berlin), and will be gradually rolled out to all locations. 

It is currently available on a request basis. To access this product, please contact your sales representative or [<mark style="color:blue;">IONOS Cloud Support</mark>](https://docs.ionos.com/support/general-information/contact-information).
{% endhint %}


### [<mark style="color:blue;">**Event Streams for Apache Kafka**</mark>](../../../data-analytics/kafka/README.md)
{% hint style="success" %}
**August 1**

IONOS introduces Event Streams for Apache Kafka, a managed solution that is fully integrated with the DCD, offering a variety of cluster sizes to accommodate the diverse requirements of different applications. With this service, you can build secure event-driven architectures. The product will initially be available only in the German data centers (Frankfurt & Berlin), and will be gradually rolled out to all locations. 

It is currently available on a request basis. To access this product, please contact your sales representative or [<mark style="color:blue;">IONOS Cloud Support</mark>](https://docs.ionos.com/support/general-information/contact-information).
{% endhint %}

### [<mark style="color:blue;">**Self-restore MariaDB Clusters from the DCD**</mark>](../../../databases/mariadb/dcd-how-tos/restore-mariadb-cluster-from-backup.md)
{% hint style="success" %}
**August 1**

The self-restoration of MariaDB clusters from a backup is possible via the DCD. It minimizes downtime and data loss in unanticipated scenarios. For more information, see [<mark style="color:blue;">Use Cases</mark>](../../../databases/mariadb/use-cases.md#scenario-2-corrupted-data-cluster).
{% endhint %}

### [<mark style="color:blue;">**VPN Gateway**</mark>](../../../network-services/vpn-gateway/README.md)
{% hint style="success" %}
**August 1**


IONOS offers a robust **VPN Gateway** feature designed to ensure secure and scalable encrypted connections between your IONOS cloud resources and remote infrastructure. This solution supports two key VPN protocols: IPSec and WireGuard, providing you with flexibility and advanced security options to meet your networking needs.

It is currently available on a request basis. To access this product, please contact your sales representative or [<mark style="color:blue;">IONOS Cloud Support</mark>](https://docs.ionos.com/support/general-information/contact-information).
{% endhint %}

### [<mark style="color:blue;">**In-Memory DB**</mark>](../../../databases/in-memory-db/README.md)
{% hint style="success" %}
**August 1**

IONOS DBaaS provides support for **In-Memory DB** instances and offers resources such as CPU cores and RAM size (GB) to create In-Memory DB instances. Additionally, the instance facilitates backup via snapshots and the option to recover data, making them highly reliable. It also facilitates cloud-based In-Memory DB instance patching and scalability.
{% endhint %}

### [<mark style="color:blue;">**CDN**</mark>](../../../network-services/cdn/README.md)
{% hint style="success" %}
**August 1**

IONOS releases **CDN**, a content delivery network service with multiple edge servers geographically well situated within the user's proximity to deliver content swiftly and securely with enhanced features such as Web Application Firewall (WAF) and  DDoS Layer 7 protection. It is currently available on a request basis. To access this product, please contact your sales representative or [<mark style="color:blue;">IONOS Cloud Support</mark>](https://docs.ionos.com/support/general-information/contact-information).
{% endhint %}

### [<mark style="color:blue;">**Access and Manage the API Gateway**</mark>](../2025/december-2025.md#api-gateway-end-of-life)
{% hint style="success" %}
**August 1**

The API Gateway offers a suite of functionalities to help you efficiently create, manage, and monitor your APIs. It provides essential features for managing and optimizing interactions between clients and backend services, ensuring secure and efficient API operations. Currently, it is only available in Berlin but will soon be rolled out to more locations. 

{% endhint %}

