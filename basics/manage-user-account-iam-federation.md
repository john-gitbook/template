# Manage User Account in IAM Federation

Once the organization IDP is onboarded to use IAM Federation, the organization's users can link their accounts to IAM Federation and unlink them whenever needed.

## Link User Account to IAM Federation

Upon linking a user account from the organization to IAM Federation, users can log in to the DCD using their organization credentials.

{% hint style="info" %}
**Prerequisites:** 
* The onboarding of the organization IDP must be successfully completed using the discovery endpoint. For more information, see [<mark style="color:blue;">Configure IAM Federation</mark>](../how-tos/configure-iam-federation.md).
* The user must already have an IONOS Cloud account. 
* The logged-in user's email address and the [<mark style="color:blue;">domain linked to the IDP</mark>](../how-tos/configure-iam-federation.md#request-domain-ownership) must match. 

{% endhint %}

To link a user's account from the organization to IONOS DCD, follow these steps:

{% stepper %}
{% step %}
### Initiate Account Linking

1\. Log in to the DCD using your IONOS Cloud account **Email** and **Password**. For more information, see [<mark style="color:blue;">Log in to the Data Center Designer</mark>](../../../../get-started/log-in-dcd.md).

2\. Go to **Menu** > **Management** > **IAM Federation**. 
{% endstep %}

{% step %}

### IDP Selection

{% hint style="info" %}
**Note:** Only IDPs onboarded by your organization for IAM Federation and matching your login email domain appear for account linking.
{% endhint %}

* In the **Managed Linked Accounts**, select **Link** under **ACTIONS** against the organization IDP user account that needs to be linked with IAM Federation. 

![Link the user account](../../../../images/management/identity-and-access-management/iam-federation/iam-federation-link-user-account.png)
{% endstep %}

{% step %}

### IDP Authentication

{% hint style="info" %}
**Note:** You are logged out of the DCD and redirected to your organization IDP to complete the authentication. 
{% endhint %}

* Enter your organization login credentials such as **Email**, **Password**, and **Sign In**. 

![User signs in on the organization page](../../../../images/management/identity-and-access-management/iam-federation/iam-federation-sign-in-user-organization.png)
{% endstep %}

{% step %}
### Authorization from IDP

* The IDP authenticates the user and authorizes the IONOS Cloud IAM Federation system to access their account information.
{% endstep %}

{% endstepper %}

{% hint style="success" %}
**Result:** 
* Your organization's user account is successfully linked with IAM Federation. 
* The user successfully signs into the DCD and is redirected to the **Manage Linked Accounts**.
{% endhint %}

![Link user account](../../../../images/management/identity-and-access-management/iam-federation/iam-federation-user-account-linked.png)


## Next steps

User can now log in to the [<mark style="color:blue;">DCD</mark>](https://dcd.ionos.com) using their organization IDP credentials. To do so, see [<mark style="color:blue;">Log in to the Data Center Designer with your Identity Provider</mark>](https://dcd.ionos.com).

## Unlink the user account from IAM Federation

{% hint style="warning" %}
**Warning:** Upon unlinking the user account from IAM Federation, users can log in to the DCD only using their IONOS Cloud account credentials.
{% endhint %}

To unlink a user's account from the organization with IONOS DCD, follow these steps:

{% include "../../../../includes/iam-federation/iam-federation-dcd-navigation.md" %}

2\. In the **Managed Linked Accounts**, select **Unlink** under **ACTIONS** against the organization IDP user account that needs to be linked with IAM Federation.

![Unlink the user account](../../../../images/management/identity-and-access-management/iam-federation/iam-federation-unlink-user-account.png)

{% hint style="success" %}
**Result:** Your user account from the organization has been successfully unlinked from IAM Federation. From then on, you can log in to the DCD only using your IONOS Cloud account credentials.
{% endhint %}

{% hint style="info" %}
**Note:** User can also unlink their account from the IDP anytime by revoking access to their account information.
{% endhint %}
