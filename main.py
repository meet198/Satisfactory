import json
from Satisfactory import calculate 

def handler(event, context):
  product = event.get('product')
  amount = event.get('amount')
  results = calculate(product, amount)
  print(results)
  return {
    'statusCode': 200,
    'body': json.dumps(results)
  }

handler(
  event={
    "product": "Iron Plate",
    "amount":  200,
  },
  context="",
)