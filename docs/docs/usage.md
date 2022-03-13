# Usage

Once you have access token with permissions. Let us do something for the data.

## Initial API by access token

```python
from pinterest import Api
p = Api(access_token="Your access token")
```

<details>
<summary>Async mode</summary>

```python
from pinterest import AsyncApi

ap = AsyncApi(access_token="Your access token")
```
</details>

## User Accounts

```python
p.user_account.get()
# UserAccount(username='merleliukun', account_type='BUSINESS')
```

<details>
<summary>Async mode</summary>

```python
await ap.user_account.get()
# UserAccount(username='merleliukun', account_type='BUSINESS')
```
</details>

## boards

```python
# list my boards
p.boards.list()
# BoardsResponse(items=[Board(id='1022106146619699845', name='City'), Board(id='1022106146619703648', name='Food')], bookmark=None)
# list my board's pins
p.boards.list_pins(board_id="1022106146619699845")
# PinsResponse(items=[Pin(id='1022106077902810180', created_at='2022-02-14T02:54:38'), Pin(id='1022106077902781601', created_at='2022-02-13T11:29:51'), Pin(id='1022106077902781616', created_at='2022-02-13T11:31:07'), Pin(id='1022106077902203823', created_at='2021-12-29T02:24:55')], bookmark=None)
```

<details>
<summary>Async mode</summary>

```python
# list my boards
await ap.boards.list()
# BoardsResponse(items=[Board(id='1022106146619699845', name='City'), Board(id='1022106146619703648', name='Food')], bookmark=None)
# list my board's pins
await ap.boards.list_pins(board_id="1022106146619699845")
# PinsResponse(items=[Pin(id='1022106077902810180', created_at='2022-02-14T02:54:38'), Pin(id='1022106077902781601', created_at='2022-02-13T11:29:51'), Pin(id='1022106077902781616', created_at='2022-02-13T11:31:07'), Pin(id='1022106077902203823', created_at='2021-12-29T02:24:55')], bookmark=None)
```
</details>

## pins

```python
# Get pin data
p.pins.get(pin_id="1022106077902810180")
# Pin(id='1022106077902810180', created_at='2022-02-14T02:54:38')
# Get pin analytics
p.pins.get_analytics(pin_id="1022106077902810180", start_date="2022-02-10", end_date="2022-02-11",metric_types="IMPRESSION")
# Analytics(all=AnalyticsAll(daily_metrics=[DailyMetric(date='2022-02-10'), DailyMetric(date='2022-02-11')]))
```

<details>
<summary>Async mode</summary>

```python
# Get pin data
await ap.pins.get(pin_id="1022106077902810180")
# Pin(id='1022106077902810180', created_at='2022-02-14T02:54:38')
# Get pin analytics
await ap.pins.get_analytics(pin_id="1022106077902810180", start_date="2022-02-10", end_date="2022-02-11",metric_types="IMPRESSION")
# Analytics(all=AnalyticsAll(daily_metrics=[DailyMetric(date='2022-02-10'), DailyMetric(date='2022-02-11')]))
```
</details>

And other apis are same as above.