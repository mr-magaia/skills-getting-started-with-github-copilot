from fastapi import FastAPI, HTTPException

app = FastAPI()

activities = {
    "soccer": {"participants": []},
    "basketball": {"participants": []},
    "tennis": {"participants": []},
}


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}