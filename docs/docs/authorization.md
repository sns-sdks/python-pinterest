# Authentication

All Pinterest API endpoints are designed to work in the context of a single operating user. We identify this user based on the access token you pass with each request. To generate a user access token, you must first request access to act on the user’s behalf through a flow based on the OAuth 2.0 authorization framework. Once you have a valid token you must include the header Authorization: Bearer {token} to make a successful request.

## Prerequisite

At the beginning, You need a Pinterest app, and be reviewed.

### Register your app and get your app id and app secret key

You can create an app by the following steps.

1. Log into [`www.pinterest.com`](https://www.pinterest.com/) with the account that you’ll use to manage your apps
2. Go to [My Apps](https://developers.pinterest.com/apps/)
3. Select `Connect app` and complete our request form with your app information.
4. Submit your request for our team to review (review our [Developer Guidelines](https://policy.pinterest.com/en/developer-guidelines) to understand what we do and don’t support with our API) You will receive an email letting you know the status of your request once we have completed the review
5. Return to My Apps to see your app id and secret key.

### Configure the redirect URI required by this code.

When you give user to do authorization, The `pinterest` will redirect a `URL` which provided by you server. And you can set up it by the following steps.

1. Click on the name of your app at [https://developers.pinterest.com/apps/](https://developers.pinterest.com/apps/). Go to the “Configure” section inside your application, and in the box labeled "Redirect URIs," enter the desired URI.
2. Save your entries.
3. If desired, you may run the sample environment set-up script and verify the results, as described in the [Pinterest API QuickStart Github Repo](https://github.com/pinterest/api-quickstart#readme).

## OAuth flow

Now you can follow our step to authorization.

!!! tip
    Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.8+ with `python -m asyncio` to try this code interactively, as they support executing `async`/`await` expressions in the console.

### Initial The API

You need `App ID`  and `App Secret` to initial Api instance.

```python
from pinterest import Api
p = Api(app_id="You app ID", app_secret="Your app secret")
```
<details>
<summary>Async mode</summary>

```python
from pinterest import AsyncApi

ap = AsyncApi(app_id="You app ID", app_secret="Your app secret")
```
</details>

By default, The redirect uri is `https://localhost/`, and scope is `["user_accounts:read", "pins:read", "boards:read"]`. You need add this redirect uri to App's Authentication settings.

### Get authorization url

Now you can get the url for user to do authenticate. And you can point the scope and redirect uri by the parameter `redirect_uri`, `scope`.

```python
p.get_authorization_url()
# ('https://www.pinterest.com/oauth?response_type=code&client_id=xxx&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=user_accounts%3Aread%2Cpins%3Aread%2Cboards%3Aread&state=un7tyObPV2zPS1PgfP8UuUKJfG66bp', 'un7tyObPV2zPS1PgfP8UuUKJfG66bp')
```

<details>
<summary>Async mode</summary>

```python
ap.get_authorization_url()
# ('https://www.pinterest.com/oauth?response_type=code&client_id=xxx&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=user_accounts%3Aread%2Cpins%3Aread%2Cboards%3Aread&state=un7tyObPV2zPS1PgfP8UuUKJfG66bp', 'un7tyObPV2zPS1PgfP8UuUKJfG66bp')
```
</details>

### Generate access token

Once you have the redirect response for your callback url, you can get the user access token.

```python
p.generate_access_token(response="Your redirect response url")
# {"access_token": "pina_xxx", "refresh_token": "pinr_xxx", "response_type": "authorization_code", 
# "token_type": "bearer", "expires_in": 2592000, "refresh_token_expires_in": 31536000, "scope": "user_accounts:read pins:read boards:read"}
```

<details>
<summary>Async mode</summary>

```python
await ap.generate_access_token(response="Your redirect response url")
# {"access_token": "pina_xxx", "refresh_token": "pinr_xxx", "response_type": "authorization_code", 
# "token_type": "bearer", "expires_in": 2592000, "refresh_token_expires_in": 31536000, "scope": "user_accounts:read pins:read boards:read"}
```
</details>

Now you can use `acess_token` to read your user accounts, pins and boards.
