# Circle API

## GET CIRCLE FUNCTIONS

`www.example.com/api/circle/page=1`

### JSON Response
- Response [200]

```json
{
    "page": "1",
    "per_page": "2",
    "total": "1",
    "total_pages": "1",
    "data": [
        {
            "radius": "x",
            "area": "pi*x**2",
            "circumference": "2*pi*x"
        }
    ]
}
```
## GET CIRCLE WIHT SPECIFIC RADIUS
- Request
`/api/circle/1`
```json
{
    "radius": "2"
}
```
- Response [201]
```json
{
    "id": "1",
    "radius" : "2",
    "area": "12.566",
    "circumference": "12.566",
    "createdAt": "2021 - 12 - 20T....."
}
```
## Create circle
...