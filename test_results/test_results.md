# datastore.py Test Results

Generated: 2026-10-13 09:07:40

| Test | Outcome | Duration (s) |
|---|---|---|
| `test_datastore.py::test_add_annual_fees_creates_fee_for_every_active_member` | FAILED | 0.0002 |
| `test_datastore.py::test_add_annual_fees_duplicate_raises_integrity_error` | FAILED | 0.0002 |
| `test_datastore.py::test_add_game` | FAILED | 0.0002 |
| `test_datastore.py::test_add_game_to_loan` | FAILED | 0.0002 |
| `test_datastore.py::test_add_loan_returns_new_loan_id` | FAILED | 0.0005 |
| `test_datastore.py::test_add_members_inserts_row` | FAILED | 0.0002 |
| `test_datastore.py::test_date_today_format` | FAILED | 0.0002 |
| `test_datastore.py::test_delete_game_removes_row` | FAILED | 0.0002 |
| `test_datastore.py::test_get_all_members_includes_inactive` | PASSED | 0.0006 |
| `test_datastore.py::test_get_catalogue_shape` | PASSED | 0.0086 |
| `test_datastore.py::test_get_catalogue_status_reflects_most_recent_loan` | FAILED | 0.0024 |
| `test_datastore.py::test_get_categories` | FAILED | 0.0002 |
| `test_datastore.py::test_get_fees` | FAILED | 0.0002 |
| `test_datastore.py::test_get_game_name_filters_case_insensitively` | PASSED | 0.0011 |
| `test_datastore.py::test_get_games_age_filters` | PASSED | 0.0012 |
| `test_datastore.py::test_get_games_available_returns_available_games` | PASSED | 0.0006 |
| `test_datastore.py::test_get_games_dropdown` | FAILED | 0.0002 |
| `test_datastore.py::test_get_games_on_hold` | PASSED | 0.0033 |
| `test_datastore.py::test_get_games_on_loan_excludes_returned` | FAILED | 0.0002 |
| `test_datastore.py::test_get_games_players_filters_range` | PASSED | 0.0008 |
| `test_datastore.py::test_get_latest_loan_id_increments` | FAILED | 0.0002 |
| `test_datastore.py::test_get_mem_held_games` | FAILED | 0.0002 |
| `test_datastore.py::test_get_member_by_email` | FAILED | 0.0004 |
| `test_datastore.py::test_get_members_games` | FAILED | 0.0005 |
| `test_datastore.py::test_get_members_only_active` | PASSED | 0.0005 |
| `test_datastore.py::test_update_fees_marks_paid` | FAILED | 0.0003 |
| `test_datastore.py::test_update_hold_toggles` | FAILED | 0.0007 |
| `test_datastore.py::test_update_loan_only_closes_open_loan` | FAILED | 0.0011 |
| `test_datastore.py::test_update_member_status_toggles` | FAILED | 0.0009 |
| `test_datastore.py::test_update_password` | FAILED | 0.0005 |

**Summary:** 8/30 passed, 22 failed
