# Create an IPSec Tunnel between two VDCs

## Overview

This tutorial demonstrates how users can configure the VPN Gateway product in IONOS Cloud to create an IPSec based site-to-site setup between two VDCs in different regions.

This tutorial demonstrates the use of the following:

| **Components**   | **Description**                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------- |
| Two VDCs         | Provisioned in locations Berlin `ionos-cloud-txl` and London `ionos-cloud-lhr` respectively.                    |
| Managed gateways | We will use a managed IPSec instance to provide secure, encrypted connectivity between two VDCs in IONOS Cloud. |

![Architecture depicts two IONOS Cloud VDCs connected over an IPSec tunnel](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-1f6ca2148c627a8ae60d1b47e33875951ead08cd%2Ftutorial-ipsec-vdc-vdc-architecture.png?alt=media)

## Target audience

This tutorial is intended to help both developers and technical decision-makers.

## What you will learn

By following this tutorial, you will learn how to:

* Provision managed IPSec VPN Gateways in IONOS Cloud across different regions.
* Configure site-to-site IPSec tunnels between two VDCs.
* Generate and use secure pre-shared keys for authentication.
* Set up LAN subnets and assign gateway addresses.
* Configure tunnel parameters including encryption, integrity, and network CIDRs.
* Manually add routing rules to enable traffic between VDCs.
* Verify secure connectivity between hosts in separate VDCs.

## Before you begin

The following information is necessary to set up an IPSec connection between two VDCs:

| **Components**             | **Berlin VPN** `ionos-cloud-txl`     | **London VPN** `ionos-cloud-lhr`                                                                                                                        |
| -------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VDC Name**               | `ionos-cloud-txl`                    | `ionos-cloud-lhr`                                                                                                                                       |
| **Gateway Public Address** | `203.0.113.10`                       | `203.0.113.20`                                                                                                                                          |
| **LAN ID**                 | `1`                                  | `2`                                                                                                                                                     |
| **LAN Subnet**             | `192.168.1.0/24`                     | `192.168.2.0/24`                                                                                                                                        |
| **Gateway Lan Address**    | `192.168.1.5`                        | `192.168.2.5`                                                                                                                                           |
| **LAN Host 1**             | `192.168.1.11`                       | `192.168.2.11`                                                                                                                                          |
| **LAN Host 2**             | `192.168.1.12`                       | `192.168.2.12`                                                                                                                                          |
| **Pre-Shared Key**         | Remember to use the appropriate key. | **Example:** `vPabcdefg123435hij565k7lmno8pq=`. This is a sample key used as an example in this document. Do not use this key for real-world scenarios. |

### Reserve your IPs

Before proceeding, ensure you have an IP block with at least one free IP address to assign to each gateway. For more information, see [<mark style="color:blue;">Reserve an IPv4 Address</mark>](https://docs.ionos.com/cloud/network-services/vdc-networking/how-tos/ip-addresses).

| **Components**             | **Berlin VPN** `ionos-cloud-txl` | **London VPN** `ionos-cloud-lhr` |
| -------------------------- | -------------------------------- | -------------------------------- |
| **Gateway Public Address** | `203.0.113.10`                   | `203.0.113.20`                   |

### Configure LAN

This tutorial uses `10.10.1.0/24` and `10.10.2.0/24` for private LANs in the IONOS Cloud. Remember to assign an IP address from the subnet to each gateway. The chosen IP address must be outside the DHCP pool and range from `.2` to `.9`.

| **Components**          | **Berlin VPN** `ionos-cloud-txl` | **London VPN** `ionos-cloud-lhr` |
| ----------------------- | -------------------------------- | -------------------------------- |
| **LAN ID**              | `1`                              | `2`                              |
| **LAN Subnet**          | `192.168.1.0/24`                 | `192.168.2.0/24`                 |
| **Gateway Lan Address** | `192.168.1.5`                    | `192.168.2.5`                    |

### Generate Pre-Shared Key (PSK)

Our current IPSec implementation supports PSK (which is expected to support certificates in the future). When provisioning gateways, ensure you generate a PSK at least 32 characters long. Optionally, you can also generate a PSK while [<mark style="color:blue;">creating an IPSec tunnel</mark>](https://docs.ionos.com/cloud/network-services/vpn-gateway/dcd-how-tos/create-peer-tunnel). The following commands explain how to generate PSK for Linux and Windows, respectively:

{% tabs %}
{% tab title="Linux" %}
Execute either of these commands:

```bash
openssl rand -base64 48
```

```bash
head -c 32 /dev/urandom | base64 
```

{% endtab %}

{% tab title="Windows" %}
```bash
$b = New-Object byte[] 32; (New-Object System.Security.Cryptography.RNGCryptoServiceProvider).GetBytes($b); [System.Convert]::ToBase64String($b) | Set-Content -Path .\psk.txt -Encoding ASCII
```
{% endtab %}
{% endtabs %}

## Procedure

{% stepper %}
{% step %}

#### Setup VDCs

Below are some screenshots from the DCD that contains the required VDCs.

**1. VDC in `ionos-cloud-txl`**

To begin with, two virtual servers are provisioned in the location `ionos-cloud-txl` and connected to each other via a private LAN. In this instance, LAN1 uses a custom subnet `192.168.1.0/24`. We designate these two servers as `192.168.1.11` and `192.168.1.12`, respectively.

![Configuration on the ionos-cloud-txl VDC](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-4a3ce15cd43378dc2d89403d0ab984e8a258b41e%2Ftutorial-ipsec-vdc-vdc-cloud-setup1.png?alt=media)

**2. VDC in `ionos-cloud-lhr`**

Similar to the `ionos-cloud-txl` VDC, two virtual servers are provisioned in `ionos-cloud-lhr` and connected to each other via a private LAN. In this instance, LAN2 uses a custom subnet `192.168.2.0/24`. We designate these two servers as `192.168.2.11` and `192.168.2.12`, respectively.

![Configuration on the ionos-cloud-lhr VDC](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-80b2fdc9a766f1bf86c8e04b0dfa1fc594707b8b%2Ftutorial-ipsec-vdc-vdc-cloud-setup2.png?alt=media)
{% endstep %}

{% step %}

#### Provision the VPN Gateways

This will need to be repeated for both sites, referring to the table of configuration parameters:

1\. In the **DCD**, go to **Menu** > **Network Services** > **VPN Gateway**.

2\. Click **Create VPN Gateway** from the **VPN Gateways** window.

3\. Enter the following details:

{% tabs %}
{% tab title="Properties" %}
Complete the properties before proceeding:

| **Components** | **Description** | **Example** |
| --- | --- | --- |
| **Name** | A descriptive name for the gateway instance, this does not need to be globally unique. Restricted to 255 characters. | `vdc-to-vdc` |
| **Location** | A list of available locations for VPN Gateway configuration. | `ionos-cloud-txl` |
| **IP Address** | A list of available public IPv4 addresses. | `203.0.113.10` |
| **Description** | More descriptive text for the gateway, limited to 1024 characters. | `VPN Gateway for creating an IPSec Tunnel between VDCs.` |

![Define properties](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-cdb807bbf58af43b8f7e8ac5218b0b622b84a73a%2Ftutorial-ipsec-vdc-vdc-properties.png?alt=media)
{% endtab %}

{% tab title="VPN Tier" %}
The **Enhanced VPN** tier is selected by default. The number of LANs and tunnels or peers differ for each tier. You can also enable **High Availability** for a chosen tier, allowing VMs to operate in an active-passive mode. It minimizes downtime during a failover and ensures an uninterrupted connection.

{% hint style="info" %}
**Note:** You can only upgrade the tier or switch between High Availability (HA) and non-HA variants during editing.
{% endhint %}

![Select a tier](../../images/vpn-gateway/tutorial-ipsec-vdc-vdc-vpn-tier.png)
{% endtab %}

{% tab title="Protocol" %}
The IPSec protocol is selected by default and no other configuration parameters are required.

![Select a protocol](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-0d4647f12d2b3641cd0dd740789314eee7e2c2df%2Ftutorial-ipsec-vdc-on-prem-dcd-protocol.png?alt=media)
{% endtab %}

{% tab title="LAN Connections" %}
Attach a VPN Gateway to LANs in IONOS Cloud. Note that it is only possible to connect to LANs in the exact location where the VPN Gateway was provisioned. Let us look at the parameters required:

| **Components**  | **Description**                                                                               | **Example**                     |
| --------------- | --------------------------------------------------------------------------------------------- | ------------------------------- |
| **Datacenter**  | Select a data center from the drop-down that lists VDCs in the same location as the gatweway. | `ionos-cloud-txl`               |
| **Connections** | A list of connected LANs and the LAN addresses.                                               | `Refer to the following table`. |

After selecting a data center, click **Add LAN Connection** to launch an additional pop-up window to set the following properties:

| **Components** | **Description**                                                         | **Example**      |
| -------------- | ----------------------------------------------------------------------- | ---------------- |
| **LAN**        | The ID of the LAN to connect to.                                        | `1`              |
| **IPv4 CIDR**  | The LAN IPv4 address assigned to the subnet's gateway in CIDR notation. | `192.168.1.5`    |
| **IPv6 CIDR**  | The LAN IPv6 address assigned to the subnet's gateway in CIDR notation. | `Not applicable` |

![LAN connections](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-b7be119a410773a8013e47e63f76d2c75fbbe883%2Ftutorial-ipsec-vdc-on-prem-dcd-lan.png?alt=media)
{% endtab %}

{% tab title="Maintenance Window" %}
Define a maintenance window to begin at the specified start time (UTC) and continue for a duration of four hours. Specify the following:

| **Components** | **Description**                                                                        | **Example** |
| -------------- | -------------------------------------------------------------------------------------- | ----------- |
| **Day**        | Select a day from the drop-down list to set a day for maintenance.                     | `Sunday`    |
| **Time**       | Enter a time using the pre-defined format (hh:mm:ss) to schedule the maintenance task. | `01:40 AM`  |

![Schedule maintenance](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-f828a723e0efe620d66e08fe6dfbbd66beb1f1c4%2Fvpn-gateway-maintenance.png?alt=media)
{% endtab %}
{% endtabs %}

4\. Click **Save** and wait for the gateway to complete provisioning. The process typically takes about 8-10 minutes, but further operations on the gateway will be instantaneous.

{% hint style="info" %}
**Note:** Repeat this process for the `ionos-cloud-lhr` location to create a managed IPSec gateway there too using the parameters table to set the required properties correctly.
{% endhint %}
{% endstep %}

{% step %}

#### Configure the VPN Tunnels

Now that the VPN Gateway instance is provisioned, the next step is to configure a tunnel to permit the two sides to talk with each other. We will need to configure a tunnel on both instances of the managed gateway.

1\. Click **Create Tunnels** to begin configuring a new tunnel.

![Configure a tunnel](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-e5113d0583b224f1396cde5ad0ba87bad62259d8%2Ftutorial-ipsec-vdc-vdc-vpn-tunnels.png?alt=media)

2\. Configure the Tunnels for `ionos-cloud-txl` and `ionos-cloud-lhr`, respectively.

**a. `ionos-cloud-txl` Tunnel Configuration**

{% tabs %}
{% tab title="Properties" %}
Enter the following details to configure a tunnel:

| **Components**  | **Description**                                                                                   | **Example**      |
| --------------- | ------------------------------------------------------------------------------------------------- | ---------------- |
| **Tunnel Name** | A name for the tunnel, this does not need to be globally unique and is limited to 255 characters. | `lhr-tunnel`     |
| **Description** | More descriptive text for the peer, limited to 1024 characters.                                   | `Not Applicable` |
| **Remote Host** | The Gateway Public IPv4 address of the remote VPN Gateway.                                        | `203.0.113.20`   |

![Configure tunnel properties](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-dc76f50a1d4fbe56cf4eeee48f42256d4329cf1e%2Ftutorial-ipsec-vdc-vdc-de-prop.png?alt=media)
{% endtab %}

{% tab title="Authentication" %}
Set the PSK as shown:

| **Components** | **Description**                        | **Example**                       |
| -------------- | -------------------------------------- | --------------------------------- |
| Pre-Shared Key | A strong key, minimum of 32 characters | `vPabcdefg123435hij565k7lmno8pq=` |

![Configure PSK](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-ae40b210546676d424d50ff8d8976332249fd005%2Ftutorial-ipsec-vd-on-prem-tunnel-psk.png?alt=media)
{% endtab %}

{% tab title="Initial Exchange" %}
This tab displays the Initial Exchange (IKE\_SA\_INIT) Settings.

{% hint style="info" %}
**Note:** Both sites typically have the same exchange settings. If the configuration differs on both sides, the two gateways will negotiate to agree on the most secure settings.
{% endhint %}

Here, you can set the various encryption and integrity algorithms, Diffie-Hellman Group, and lifetimes for the IKE exchange phase. For the purposes of the demonstration, the available options are aligned with BSI best practices. However, we will accept the default selections.

| **Components**           | **Description**                                                                                                                                                                                                                                                                                                                                                           | **Example**   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Encryption Algorithm** | Encryption algorithms protect the data so it cannot be read by a third-party while in transit.                                                                                                                                                                                                                                                                            | `AES128-CTR`  |
| **Integrity Algorithm**  | Integrity algorithms provide authentication of messages and randomness, ensuring that packets are authentic and were not altered by a third party before arriving, and also for constructing keying material for encryption.                                                                                                                                              | `SHA256`      |
| **Diffe-Hellman**        | The Diffie-Hellman (DH) key exchange algorithm is a method used to make a shared encryption key available to two entities without an exchange of the key. The encryption key for the two devices is used as a symmetric key for encrypting data. Only the two parties involved in the DH key exchange can deduce the shared key, and the key is never sent over the wire. | `15-MODP3072` |
| **Lifetime**             | The length of time (in seconds) that a negotiated IKE SA key is effective. Before the key lifetime expires, the SA must be re-keyed; otherwise, upon expiration, the SA must begin a new IKEv2 IKE SA re-key.                                                                                                                                                             | `86400`       |

![Select a suitable algorithm](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-9f67f27fafa9839cb3bae93706998613d0bd50d3%2Ftutorial-ipsec-vd-on-prem-tunnel-algorithm.png?alt=media)
{% endtab %}

{% tab title="Child SA/IPSec" %}
This tab displays the Child SA/IPSec SA Settings (ESP) settings.

{% hint style="info" %}
**Note:** Both sites typically have the same ESP settings. If the configuration differs on both sides, the two gateways will negotiate to agree on the most secure settings.
{% endhint %}

Here, you can set the various encryption and integrity algorithms, Diffie-Hellman Group, and lifetimes for the ESP phase. For the purposes of the demonstration, the available options are aligned with BSI best practices. However, we will accept the default selections.

| **Components**           | **Description**                                                                                                                                                                                                                                                                                                                                                           | **Example**   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Diffe-Hellman**        | The Diffie-Hellman (DH) key exchange algorithm is a method used to make a shared encryption key available to two entities without an exchange of the key. The encryption key for the two devices is used as a symmetric key for encrypting data. Only the two parties involved in the DH key exchange can deduce the shared key, and the key is never sent over the wire. | `15-MODP3072` |
| **Encryption Algorithm** | Encryption algorithms protect the data so it cannot be read by a third-party while in transit.                                                                                                                                                                                                                                                                            | `AES128-CTR`  |
| **Integrity Algorithm**  | Integrity algorithms provide authentication of messages and randomness, ensuring that packets are authentic and were not altered by a third party before arriving, and also for constructing keying material for encryption.                                                                                                                                              | `SHA256`      |
| **Lifetime**             | The ESP SA determines how long the keys generated during the IKE negotiation are valid for encrypting and authenticating the actual data packets being transmitted.                                                                                                                                                                                                       | `3600`        |

![Select a suitable algorithm](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-b115fc4a18a5a83d14198f344ee9e4bf466dd50f%2Ftutorial-ipsec-vd-on-prem-child-sa-settings.png?alt=media)
{% endtab %}

{% tab title="Network CIDRs" %}
Configure the subnets in CIDR format, which are permitted to connect to the tunnel.

{% hint style="info" %}
**Note:** You may use `0.0.0.0/0` to permit any network; however, one site should explicitly define the network CIDRs permitted. Using `0.0.0.0/0` on both VPN gateways will result in broken routing.
{% endhint %}

| **Components** | **Description** | **Example** |
| --- | --- | --- |
| **Cloud Network CIDRs** | Network addresses on the cloud side that are permitted to connect to the tunnel. | `192.168.1.0/24` |
| **Peer Network CIDRs** | Network addresses on the peer side that are permitted to connect to the tunnel. | `192.168.2.0/24` |

![Configure PSK](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-348ca546a5e373d240bd9b3f9f265c155d78b1d0%2Ftutorial-ipsec-vdc-vdc-network-cidr.png?alt=media)
{% endtab %}
{% endtabs %}

**b. `ionos-cloud-lhr` Tunnel Configuration**

{% tabs %}
{% tab title="Properties" %}
Enter the following details to configure a tunnel:

| **Components**  | **Description**                                                                                   | **Example**    |
| --------------- | ------------------------------------------------------------------------------------------------- | -------------- |
| **Tunnel Name** | A name for the tunnel, this does not need to be globally unique and is limited to 255 characters. | `txl-tunnel`   |
| **Description** | More descriptive text for the peer, limited to 1024 characters.                                   | `N/A`          |
| **Remote Host** | The Gateway Public IPv4 address of the remote VPN Gateway.                                        | `203.0.113.10` |

![Configure tunnel properties](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-85be2df3d71838cd3040f98e94cfa04b94532a0e%2Ftutorial-ipsec-vdc-vdc-gb-prop.png?alt=media)
{% endtab %}

{% tab title="Authentication" %}
**3.2 Authentication**

This is where the Pre-shared key (PSK) is set.

| **Components**     | **Description**                         | **Example**                       |
| ------------------ | --------------------------------------- | --------------------------------- |
| **Pre-Shared Key** | A strong key, minimum of 32 characters. | `vPabcdefg123435hij565k7lmno8pq=` |

![Configure PSK](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-ae40b210546676d424d50ff8d8976332249fd005%2Ftutorial-ipsec-vd-on-prem-tunnel-psk.png?alt=media)
{% endtab %}

{% tab title="Initial Exchange" %}
This tab displays the Initial Exchange (IKE\_SA\_INIT) Settings.

{% hint style="info" %}
**Note:** Both sites typically have the same exchange settings. If the configuration differs on both sides, the two gateways will negotiate to agree on the most secure settings.
{% endhint %}

Here, you can set the various encryption and integrity algorithms, Diffie-Hellman Group, and lifetimes for the IKE exchange phase. For the purposes of the demonstration, the available options are aligned with BSI best practices. However, we will accept the default selections.

| **Components**           | **Description**                                                                                                                                                                                                                                                                                                                                                           | **Example**   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Diffe-Hellman**        | The Diffie-Hellman (DH) key exchange algorithm is a method used to make a shared encryption key available to two entities without an exchange of the key. The encryption key for the two devices is used as a symmetric key for encrypting data. Only the two parties involved in the DH key exchange can deduce the shared key, and the key is never sent over the wire. | `15-MODP3072` |
| **Encryption Algorithm** | Encryption algorithms protect the data so it cannot be read by a third-party while in transit.                                                                                                                                                                                                                                                                            | `AES128-CTR`  |
| **Integrity Algorithm**  | Integrity algorithms provide authentication of messages and randomness, ensuring that packets are authentic and were not altered by a third party before arriving, and also for constructing keying material for encryption.                                                                                                                                              | `SHA256`      |
| **Lifetime**             | The length of time (in seconds) that a negotiated IKE SA key is effective. Before the key lifetime expires, the SA must be re-keyed; otherwise, upon expiration, the SA must begin a new IKEv2 IKE SA re-key.                                                                                                                                                             | `86400`       |

![Select a suitable algorithm](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-9f67f27fafa9839cb3bae93706998613d0bd50d3%2Ftutorial-ipsec-vd-on-prem-tunnel-algorithm.png?alt=media)
{% endtab %}

{% tab title="Child SA/IPSec" %}
This tab displays the Child SA/IPSec SA Settings (ESP) settings.

{% hint style="info" %}
**Note:** Both sites typically have the same ESP settings. If the configuration differs on both sides, the two gateways will negotiate to agree on the most secure settings.
{% endhint %}

Here, you can set the various encryption and integrity algorithms, Diffie-Hellman Group, and lifetimes for the ESP phase. For the purposes of the demonstration, the available options are aligned with BSI best practices. However, we will accept the default selections.

| **Components**           | **Description**                                                                                                                                                                                                                                                                                                                                                           | **Example**   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Diffie-Hellman**       | The Diffie-Hellman (DH) key exchange algorithm is a method used to make a shared encryption key available to two entities without an exchange of the key. The encryption key for the two devices is used as a symmetric key for encrypting data. Only the two parties involved in the DH key exchange can deduce the shared key, and the key is never sent over the wire. | `15-MODP3072` |
| **Encryption Algorithm** | Encryption algorithms protect the data so it cannot be read by a third party while in transit.                                                                                                                                                                                                                                                                            | `AES128-CTR`  |
| **Integrity Algorithm**  | Integrity algorithms provide authentication of messages and randomness, ensuring that packets are authentic and were not altered by a third party before arriving, and also for constructing keying material for encryption.                                                                                                                                              | `SHA256`      |
| **Lifetime**             | The ESP SA determines how long the keys generated during the IKE negotiation are valid for encrypting and authenticating the actual data packets being transmitted.                                                                                                                                                                                                       | `3600`        |

![Select a suitable algorithm](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-b115fc4a18a5a83d14198f344ee9e4bf466dd50f%2Ftutorial-ipsec-vd-on-prem-child-sa-settings.png?alt=media)
{% endtab %}

{% tab title="Network CIDRs" %}
Configure the subnets in CIDR format, which are permitted to connect to the tunnel.

{% hint style="info" %}
**Note:** You may use `0.0.0.0/0` to permit any network; however, one site should explicitly define the network CIDRs permitted. Using `0.0.0.0/0` on both VPN gateways will result in broken routing.
{% endhint %}

| **Components** | **Description** | **Example** |
| --- | --- | --- |
| **Cloud Network CIDRs** | Network addresses on the cloud side that are permitted to connect to the tunnel. | `192.168.2.0/24` |
| **Peer Network CIDRs** | Network addresses on the peer side that are permitted to connect to the tunnel. | `192.168.1.0/24` |

![Configure PSK](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-348ca546a5e373d240bd9b3f9f265c155d78b1d0%2Ftutorial-ipsec-vdc-vdc-network-cidr.png?alt=media)
{% endtab %}
{% endtabs %}

3\. Click **Save** to save the tunnel configuration. This operation usually takes about one to two minutes to complete.
{% endstep %}

{% step %}

#### Configure routing on LAN hosts

Currently, it is impossible to automate the addition of routes to LAN hosts to route the required subnets over the VPN Gateway. In this section, we will manually add the required routes. Remember to add them to the LAN hosts in both VDCs.

**1. Configure `ionos-cloud-txl` route**

<details>

<summary><strong>Step 1: Establish a console session to the LAN host(s)</strong></summary>

We will use the web console to test connectivity for the LAN hosts without internet access. Open a console session and ping the LAN address assigned to the VPN Gateway, `192.168.1.5`. Begin by pinging the IP address:

```bash
root@berlinlanhost1:~# ping -c 3 192.168.1.5 
PING 192.168.1.5 (192.168.1.5) 56(84) bytes of data.
64 bytes from 192.168.1.5 icmp_seq=1 ttl=64 time=0.456 ms
64 bytes from 192.168.1.5 icmp_seq=2 ttl=64 time=0.352 ms
64 bytes from 192.168.1.5 icmp_seq=3 ttl=64 time=0.503 ms

--- 192.168.1.5 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2019ms
rtt min/avg/max/mdev = 0.352/0.437/0.503/0.063 ms
root@berlinlanhost1:~#
```

</details>

<details>

<summary><strong>Step 2: Configure the VPN route</strong></summary>

The LAN host(s) must know where to route the return traffic. To accomplish this, we will add a route for the `ionos-cloud-lhr` LAN subnet `192.168.2.0/24` via the `ionos-cloud-txl` gateway's LAN address `192.168.1.5`:

```bash
ip route add 192.168.2.0/24 via 192.168.1.5
```

We cannot ping hosts in the `ionos-cloud-lhr` region because those servers do not yet know how to route the return traffic. To resolve this issue, continue adding routes for LAN hosts in `ionos-cloud-lhr`.

</details>

**2. Configure `ionos-cloud-lhr` route**

<details>

<summary><strong>Step 1: Establish a console session to the LAN host(s)</strong></summary>

We will use the web console to test connectivity for the LAN hosts that does not have an internet access. Open a console session and ping the LAN address assigned to the VPN Gateway, `192.168.2.5`. Begin by pinging the IP address:

```bash
root@berlinlanhost1:~# ping -c 3 192.168.2.5 
PING 192.168.2.5 (192.168.2.5) 56(84) bytes of data.
64 bytes from 192.168.2.5 icmp_seq=1 ttl=64 time=1.34 ms
64 bytes from 192.168.2.5 icmp_seq=2 ttl=64 time=0.429 ms
64 bytes from 192.168.2.5 icmp_seq=3 ttl=64 time=0.377 ms

--- 192.168.2.5 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2019ms
rtt min/avg/max/mdev = 0.377/0.715/1.340/0.442 ms
root@berlinlanhost1:~#
```

</details>

<details>

<summary><strong>Step 2: Configure the VPN route</strong></summary>

The LAN host(s) must know where to route the return traffic. To accomplish this, we will add a route for the `ionos-cloud-txl` LAN subnet `192.168.1.0/24` via the `ionos-cloud-lhr` gateway's LAN address `192.168.2.5`:

```bash
ip route add 192.168.1.0/24 via 192.168.2.5
```

At this point, full connectivity between the two sites via the VPN Gateway is established.

</details>
{% endstep %}
{% endstepper %}

### Final result

You should now be able to ping from hosts in `ionos-cloud-txl` to hosts in `ionos-cloud-lhr`.

![Verify connectivity](https://3040852435-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEpuEvuLJIyhyeRGhmrv1%2Fuploads%2Fgit-blob-643494e3aac1812a41de37846a557b98c1dd89fe%2Ftutorial-ipsec-vdc-vdc-verify-connectivity.png?alt=media)

## Conclusion

You have successfully configured a site-to-site IPSec VPN between two IONOS Cloud VDCs using a Managed VPN Gateway.
