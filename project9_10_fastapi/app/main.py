from fastapi import FastAPI, Depends, HTTPException
from . import models, crud
from .mydb import db_connection
import logging



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title="Inventory Management API",
    description="REST API for managing inventory data. Supports full CRUD and analytics endpoints.",
    version="1.0.0"
)
# GET /inventory
@app.get("/inventory", response_model=list[models.ItemResponse])
def get_all(db=Depends(db_connection)):
    logger.info('GET/inventory')
    return crud.get_all_items(db)

# GET /inventory/{id}
@app.get('/inventory/{item_id}',response_model=list[models.ItemResponse])
def get_id(item_id: int, db=Depends(db_connection)):
    item = crud.get_item_by_id(db, item_id)
    logger.info('GET/inventory/%s', item_id)
    if item is None:
        logger.warning("Item not found: id=%s", item_id)
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# POST /inventory
@app.post("/inventory", response_model=models.ItemResponse, status_code=201)
def create(item: models.Item, db=Depends(db_connection)):
    logger.info('POST/inventory/%s', item)
    return crud.create_item(db, item)

# PUT /inventory/{id}
@app.put("/inventory/{item_id}", response_model=models.ItemResponse)
def update(item_id: int, item: models.ItemUpdate, db=Depends(db_connection)):
    updated = crud.update_item(db, item_id, item)
    logger.info('PUT/inventory/%s',item_id)
    if updated is None:
        logger.warning('Item not found: id =%s', item_id)
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

# DELETE /inventory/{id}
@app.delete("/inventory/{item_id}")
def delete(item_id: int, db=Depends(db_connection)):
    deleted = crud.delete_item(db, item_id)
    logger.info('DELETE/inventory/%s',item_id)
    if not deleted:
        logger.warning('Delete failed, inventory not found: id=%s', item_id)
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
#
# GET /analytics/category_totals
@app.get("/analytics/category_totals")
def category_totals(db=Depends(db_connection)):
    logger.info('GET/analytics/category_totals')
    return crud.get_category_totals(db)

# GET /analytics/highest_value_item
@app.get("/analytics/highest_value_item")
def highest_value_item(db=Depends(db_connection)):
    logger.info('GET/analytics/highest_value_item')
    return crud.get_highest_value_item(db)
#
# GET /analytics/total_inventory_value
@app.get("/analytics/total_inventory_value")
def total_inventory_value(db=Depends(db_connection)):
    logger.info('GET/analytics/total_inventory_value')
    return crud.get_total_inventory_value(db)