import qjph
import pytest

def test_json():
    # Example test case for qjph functionality
    data = qjph.loads("""
{
    "json": {
        "text": "value",
        "number": 42,
    }
}
""")
    assert data["json"]["text"] == "value"
    assert data["json"]["number"] == 42

if __name__ == "__main__":
    pytest.main()