from commands import add, modify, rm, show
from task import Task


def test_add():
    """Test add function"""
    tasklist = {}
    
    # Test valid add
    result = add(tasklist, "Test task", "started")
    assert len(tasklist) == 1
    assert tasklist[1].description == "Test task"
    assert tasklist[1].state == "started"
    assert "[success]" in result
    print("test_add_valid passed")
    
    # Test invalid state
    tasklist2 = {}
    result = add(tasklist2, "Test task", "invalid")
    assert len(tasklist2) == 0
    assert "[error]" in result
    print("test_add_invalid_state passed")


def test_modify():
    """Test modify function"""
    tasklist = {}
    add(tasklist, "Original task", "started")
    
    # Test modify description
    result = modify(tasklist, 1, description="Modified task")
    assert tasklist[1].description == "Modified task"
    assert "[success]" in result
    print("test_modify_description passed")
    
    # Test modify state
    result = modify(tasklist, 1, state="completed")
    assert tasklist[1].state == "completed"
    assert "[success]" in result
    print("test_modify_state passed")
    
    # Test invalid task ID
    result = modify(tasklist, 999, description="Test")
    assert "[error]" in result
    print("test_modify_invalid_id passed")


def test_rm():
    """Test rm function"""
    tasklist = {}
    add(tasklist, "Test task", "started")
    
    # Test remove existing task
    result = rm(tasklist, 1)
    assert len(tasklist) == 0
    assert "[success]" in result
    print("test_rm_existing passed")
    
    # Test remove non-existing task
    result = rm(tasklist, 999)
    assert result is None
    print("test_rm_nonexisting passed")


def test_show():
    """Test show function"""
    tasklist = {}
    
    # Test empty list
    result = show(tasklist)
    assert "[success]" in result
    print("test_show_empty passed")
    
    # Test with tasks
    add(tasklist, "Task 1", "started")
    result = show(tasklist)
    assert "[success]" in result
    print("test_show_with_tasks passed")


def run_all_tests():
    """Run all tests"""
    print("Running tests...")
    try:
        test_add()
        test_modify()
        test_rm()
        test_show()
        print("\n All tests passed!")
    except AssertionError as e:
        print(f"\n Test failed: {e}")
    except Exception as e:
        print(f"\n Error running tests: {e}")


if __name__ == "__main__":
    run_all_tests()