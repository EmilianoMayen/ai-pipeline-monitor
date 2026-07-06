from database.database import Database
from simulator.pipeline_generator import generate_pipelines


def main():

    print("Creating database...")

    db = Database()

    db.create_tables()

    print("Generating pipelines...")

    pipelines = generate_pipelines(100)

    print("Saving pipelines...")

    for pipeline in pipelines:
        db.insert_pipeline(pipeline)

    print(f"{len(pipelines)} pipelines inserted successfully!")


if __name__ == "__main__":
    main()
