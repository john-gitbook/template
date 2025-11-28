{% tabs %}
{% tab title="Verbose options" %}
```liquid
{% action "cache" %}
  {
    "set": {
      "key": "foo",
      "value": 5
    }
  }
{% endaction %}
```
{% endtab %}

{% tab title="Positional options" %}
```liquid
{% action "cache", "set", "foo", 5 %}
```
{% endtab %}
{% endtabs %}
