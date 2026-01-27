# API How-Tos

The Cloud API lets you manage Cloud GPU VMs programmatically using conventional HTTP requests. You can use the API to create, delete, and retrieve information about your Cloud GPU VMs.

Furthermore, you need templates to provision Cloud GPU VMs, but templates are not compatible with servers that support full flex configuration.

## Cloud GPU VM workflow 
To get started with Cloud GPU, follow these steps: 

{% stepper %}
{% step %} 
<h3>Request access</h3>

Cloud GPU VM is not activated automatically to ensure the configuration matches your environment requirements. Please contact the [<mark style="color:blue;">IONOS Cloud Support</mark>](https://docs.ionos.com/support/general-information/contact-information) first and request access to the service. The support team will apply the required settings so the product works perfectly from the moment it is turned on.
{% endstep %} 

{% step %} 
<h3>Discovery and selection</h3>

Cloud GPU VMs are available in preconfigured sizes. Select a template that fits best to your needs and matches your contract's resource limits, which will be adjusted as part of the access enablement process. It is not possible to change the size of a Cloud GPU VM instance once it has been provisioned. 

* [<mark style="color:blue;">List all Cloud GPU VM templates</mark>](retrieve-template-list.md). 

* Review Cloud GPU VM template specifications to select the appropriate template for your needs.

* Use the template `UUID` to make an API request call for creating a new Cloud GPU VM. 
{% endstep %} 

{% step %} 
<h3>Create a Cloud GPU VM</h3>

Initiate a [<mark style="color:blue;">Cloud GPU VM creation request</mark>](create-cloud-gpu-vm.md) through API with the following:

* The selected GPU template `UUID`
* Linux-based operating system

{% hint style="info" %}
**Note:** The product supports only Linux-based operating systems during the launch.
{% endhint %}

* Network settings
* [<mark style="color:blue;">SSH keys</mark>](../../../../security/ssh-key-manager/README.md), [<mark style="color:blue;">Cloud-init</mark>](../../how-tos/boot-cloud-init.md) script, or other authentication methods

{% hint style="success" %}
**Result:** The VM with the attached GPU is provisioned. 
{% endhint %}
{% endstep %} 

{% step %} 
<h3>Access and setup</h3>

* Connect to VM using one of the following options:
  * [<mark style="color:blue;">Through the SSH</mark>](../../how-tos/connect-vm-via-ssh.md).
  * [<mark style="color:blue;">Through the remote console</mark>](../../how-tos/connect-remote-console.md).

* Install NVIDIA drivers. For more information, refer to the [<mark style="color:blue;">NVIDIA documentation</mark>](https://www.nvidia.com/en-us/drivers/).

* Run the following command in your terminal or command prompt to verify if the Cloud GPU VM is accessible: `nvidia-smi`

{% hint style="success" %}

**Result:** 
A successful output should display the driver version, the GPU model(s), the GPU temperature, and the current memory usage. If the command is not found or returns an error, your drivers may be missing or the GPU is not properly installed.

{% endhint %}

* Install required framework dependencies. Use a package manager like `pip` or `conda` to install your chosen framework, ensuring you select the GPU-enabled version.

{% tabs %}
{% tab title="For PyTorch" %}
Install the version that matches your CUDA toolkit. For example, CUDA 12.1. 
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
{% endtab %}

{% tab title="For TensorFlow" %}
Install the standard package. It automatically detects and uses CUDA if installed correctly. 
```bash
pip install tensorflow
```
{% endtab %}
{% endtabs %}

* Use the server for your use case 
{% endstep %} 

{% step %} 
<h3>Usage</h3>

* Run GPU workloads, such as model training (finetuning), inference, or graphics rendering
* Monitor GPU utilization and performance metrics
{% endstep %} 

{% step %} 
<h3>Management</h3>

* Start, restart, or delete the Cloud GPU VM as needed. 
* Monitor costs and usage. For more information, see [<mark style="color:blue;">Cost Alert</mark>](../../../../management/usage/cost-alert.md) and [<mark style="color:blue;">Cost & Usage</mark>](../../../../management/usage/cost-and-usage.md).
{% endstep %} 

{% step %} 
<h3>Cleanup</h3>

* Back up your results and data. For more information, see [<mark style="color:blue;">Install Acronis Backup Agent on Linux</mark>](../../../../storage-&-backup/backup-service/how-tos/install-acronis-backup-agent.md). 

* [<mark style="color:blue;">Delete the Cloud GPU VM</mark>](delete-cloud-gpu-vm.md) from the VDC.
{% endstep %} 
{% endstepper %}

## Quick Links

<table data-view="cards">
    <thead>
        <tr>
            <th></th>
            <th></th>
            <th data-hidden data-card-target data-type="content-ref"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><mark style="color:blue;"><strong>Retrieve Template list</strong></mark></td>
            <td>Learn how to retrieve a list of available templates.</td>
            <td><a href="retrieve-template-list.md">retrieve-template-list</a></td>
        </tr>
        <tr>
            <td><mark style="color:blue;"><strong>Retrieve Template details</strong></mark></td>
            <td>Learn how to retrieve details of a specific template.</td>
            <td><a href="retrieve-a-template.md">retrieve-a-template</a></td>
        </tr>
        <tr>
            <td><mark style="color:blue;"><strong>Create a Cloud GPU VM</strong></mark></td>
            <td>Learn how to create a Cloud GPU VM.</td>
            <td><a href="create-cloud-gpu-vm.md">create-cloud-gpu-vm</a></td>
        </tr>
        <tr>
            <td><mark style="color:blue;"><strong>Delete a Cloud GPU VM</strong></mark></td>
            <td>Learn how to delete a Cloud GPU VM.</td>
            <td><a href="delete-cloud-gpu-vm.md">delete-cloud-gpu-vm</a></td>
        </tr>
    </tbody>
</table>

