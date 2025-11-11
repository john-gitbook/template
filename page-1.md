# Page 1

Stepper blocks let you break down a tutorial or guide into seprate, but clearly linked steps. Each step can contain multiple different blocks, allowing you to add detailed information. Just adding some content here!

#### Example

{% stepper %}
{% step %}
### Add a stepper blck

To add a stepper block, hit `/` on an empty line or click the `+` on the left of the editor and select **Stepper** from the insert menu.

{% hint style="info" %}
here is a hint block within a stepper
{% endhint %}
{% endstep %}

{% step %}
### Add some content

Once you’ve inserted your stepper block, you can start adding content to it — including code blocks, drawings, images and much more.

{% hint style="warning" %}
More information is added in this block
{% endhint %}


{% endstep %}

{% step %}
### Add more steps

Click the `+` below the step numbers or hit `Enter` twice to add another step to your stepper block. You can remove or change the style of the step header or step body if you wish.

```python
print("Hello, World!")





```
{% endstep %}

{% step %}
### Another steps

Hi there
{% endstep %}
{% endstepper %}
