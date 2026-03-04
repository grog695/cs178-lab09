import boto3
from boto3.dynamodb.conditions import Key, Attr

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "NBA_Draft_Prospects"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_prospect(prospect):

    rank = prospect.get("Rank", "Unknown Ranking")
    name = prospect.get("Name", "Unknown Name")
    
    draft_team = prospect.get("Draft Team", "No pre-draft team")
    position = prospect.get("Position", "Unknown position")
    
    print(f"  Rank          : {rank}")
    print(f"  Name          : {name}")
    print(f"  Pre-Draft Team: {draft_team}")
    print(f"  Position      : {position}")
    print()


def print_all_prospects():

    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No prospects found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} prospect(s):\n")
    for prospect in items:
        print_prospect(prospect)

def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_prospects()


if __name__ == "__main__":
    main()