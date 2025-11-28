# Page 1

{% openapi-operation spec="gitbook-petstore" path="/pets" method="get" %}
[OpenAPI gitbook-petstore](https://gitbookio.github.io/onboarding-template-images/gitbook-petstore.yaml)
{% endopenapi-operation %}

{% tabs %}
{% tab title="Verbose options" %}

```liquid
{% action "cache" %}
  {
    "setex": {
      "key": "foo",
      "ttl": 60,
      "value": 5
    }
  }
{% endaction %}
```

{% endtab %}
