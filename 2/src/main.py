from fastapi import FastAPI, Query

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/filter")
async def filter_values(
    min_value: int = Query(default=0, ge=0, alias="min"),
    max_value: int = Query(default=100, le=100, alias="max")
):
    return {"min": min_value, "max": max_value}
# END
