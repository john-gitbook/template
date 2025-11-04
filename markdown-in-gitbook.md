# Markdown in GitBook

## Headings, Paragraphs and Formatting

## Heading 1

### Heading 2

#### Heading 3

This is just a standard paragraph.

**Bold**

_**Italics**_

~~_**Strikethrough**_~~

<sup>Superscript</sup>

<sub>Subscript</sub>

[This is going to be annotated](#user-content-fn-1)[^1]

<mark style="color:green;">This text is highlighted but it could also be highligted any other colour like</mark> <mark style="color:yellow;">yellow</mark>

<mark style="background-color:blue;">This text has a blue background colour added</mark>

## Lists and steppers:



* This is unordered list item 1
* This is unordered list item 2

1. This is an ordered list item
2. This another ordered list item

* [ ] This is a task list item. It has not been checked.
* [x] This is another taks list item and has been checked.

{% stepper %}
{% step %}
### This is step 1 in a stepper block

Here's some content for the step block
{% endstep %}

{% step %}
### This is step 2 in a stepper block

Here's some more content for the step block
{% endstep %}
{% endstepper %}

## Links:

[This](https://gitbook.com/) is an incline link to the GitBook website.&#x20;

Below I will add a page link:

{% content-ref url="basics/editor.md" %}
[editor.md](basics/editor.md)
{% endcontent-ref %}

[This](basics/editor.md#writing-content) is a link to another page in this repo.

Below is an embeded URL. In this case it is an embed of a Youtube video:

{% embed url="https://www.youtube.com/watch?v=2T04FzqziEI" %}

## Hint Blocks

{% hint style="info" %}
This is an info hint block
{% endhint %}

{% hint style="warning" %}
This is a warning hint block
{% endhint %}

{% hint style="danger" %}
This is a danger hint block
{% endhint %}

{% hint style="success" %}
This is a success hint block
{% endhint %}

## Tables, Tabs, Code Blocks, Cards and Expandables

| Header Column 1 | Header Column 2 |
| --------------- | --------------- |
| row 1           | row 1           |
| row 2           | row 2           |

{% tabs %}
{% tab title="First Tab" %}
This is content within a tab
{% endtab %}

{% tab title="Second Tab" %}
This is content within a second tab
{% endtab %}
{% endtabs %}

```markup
This is a code block with the language choosen as Markup.
```

You can insert code blocks in tabs. Below this I will include a tab with multiple code blocks.

{% tabs %}
{% tab title="JavaScript" %}
```javascript
const message = "hello world";
console.log(message);
```
{% endtab %}

{% tab title="Python" %}
```python
message = "hello world"
print(message)
```
{% endtab %}

{% tab title="Ruby" %}
```ruby
message = "hello world"
puts message
```
{% endtab %}
{% endtabs %}

Below is a card with a card title and card image.&#x20;

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td>This is a Card Title</td><td><a href="https://images.unsplash.com/photo-1760624876599-a29c55487fed?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjIyNzI3ODh8&#x26;ixlib=rb-4.1.0&#x26;q=85">https://images.unsplash.com/photo-1760624876599-a29c55487fed?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjIyNzI3ODh8&#x26;ixlib=rb-4.1.0&#x26;q=85</a></td></tr></tbody></table>

<details>

<summary>Here is a title of an expandable</summary>

This is the text within the expandable

</details>



## Other blocks:

Below this text there is a divider

***

> This is a quote block. Not a very interesting quote.

<a href="markdown-in-gitbook.md#heading-1" class="button primary">This is a primary button</a>&#x20;

<a href="markdown-in-gitbook.md#headings-paragraphs-and-formatting" class="button secondary">This is a secondary button</a>



[^1]: this is my annotation
