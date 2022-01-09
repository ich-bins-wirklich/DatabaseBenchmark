from coordinator_service import CoordinatorService
from repair_service import RepairService

if __name__ == '__main__':
    # repair_service = RepairService()
    # repair_service.repair_indices_q22c()
    coordinator_service = CoordinatorService()
    coordinator_service.run_all_tests_all_queries()
