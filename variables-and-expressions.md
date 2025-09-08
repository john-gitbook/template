---
icon: icons
---

# Variables and Expressions

With variables you can create reusable text that can be conditionally referenced in [expressions](broken-reference) and [conditions for adaptive content](broken-reference).&#x20;

If you repeat the same name, phrase or version number multiple times within your content, you can create a **variable** to help keep all those instances in sync and accurate — which is useful if you ever need to update them, or they’re complex and often mistyped.

You can create variables that are scoped to a single page, or a single space.

### Create a new variable

To create a new variable, Click the **Variables** <picture><source srcset="broken-reference" media="(prefers-color-scheme: dark)"><img src=".gitbook/assets/variables.svg" alt=""></picture> icon in the upper right corner when editing an open [change request](broken-reference). This will open the Variables side panel.

You can use the toggle at the top to view and create variables scoped either to the current page you’re on, or all pages within the current space.

Clicking **Create a variable** will launch a modal where you can give your variable a name and a value.

Click **Add variable** to save your variable.

<figure><img src=".gitbook/assets/variables.jpg" alt="A GitBook screenshot showing the Add variables screen. The variable Name box has been filled with the text ‘latest_version’ and the Value box has been filled with the text ‘v3.04.1’"><figcaption><p>You can add variables to a single page or an entire space. When you update the value of a variable, every instance of it will update.</p></figcaption></figure>

{% hint style="info" %}
Variable names must start with a letter, and can contain letters, numbers and underscores.
{% endhint %}

### Use variables in your content

Variables can be referenced and used within an [expression](broken-reference) — which you can insert into your content inline. After inserting an expression, double click it to open the expression editor.

Variables defined under your page are accessible under the `page.vars` object. Similarly, variables defined across your entire space are accessible under the `space.vars` object.&#x20;

<figure><img src=".gitbook/assets/insert-variables-expression.jpg" alt="A GitBook screenshot showing an expression block within the editor. The expression editor is open below it and the ‘space.vars.latest_version’ variable has been selected"><figcaption><p>You can add variables to your content within expresions. The expression editor offers autocomplete options to help you find the variable you need.</p></figcaption></figure>

### Update a variable

You can update a variable at any point when within a change request. Updating its value will update the value across any expression blocks referencing it. The changed variable will go live to any published site once the change request is merged.
