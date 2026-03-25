"""
Author > TeijiW
Code to calculate some data about employees of company
"""

import json
import os


def calculate_salary(data):
    """
    Function to calculate max, min and average company salaries
    """
    salaries = []
    _ = [salaries.append(employee["salario"]) for employee in data["funcionarios"]]
    max_salary = max(salaries)
    min_salary = min(salaries)
    average_salary = sum(salaries) / len(salaries)
    _ = [
        print(
            "global_max|{}|{}".format(
                employee["nome"] + " " + employee["sobrenome"], employee["salario"]
            )
        )
        for employee in data["funcionarios"]
        if employee["salario"] == max_salary
    ]
    _ = [
        print(
            "global_min|{}|{}".format(
                employee["nome"] + " " + employee["sobrenome"], employee["salario"]
            )
        )
        for employee in data["funcionarios"]
        if employee["salario"] == min_salary
    ]
    print("global_avg|{:.2f}".format(average_salary))


def calculate_salary_by_area(data):
    """
    Function to calculate salary max, min and average by area
    """
    area_list = [area_dict["codigo"] for area_dict in data["areas"]]
    area_name_dict = {
        area_dict["codigo"]: area_dict["nome"] for area_dict in data["areas"]
    }
    employee_by_area = {key: [] for key in area_list}
    for employee in data["funcionarios"]:
        employee_by_area[employee["area"]].append(employee)
    for key in employee_by_area:
        salaries = []

        _ = [salaries.append(employee["salario"]) for employee in employee_by_area[key]]
        if len(salaries) > 0:
            max_salary = max(salaries)
            min_salary = min(salaries)
            average_salary = sum(salaries) / len(salaries)
        else:
            max_salary = 0
            min_salary = 0
            average_salary = 0
        _ = [
            print(
                "area_max|{}|{}|{}".format(
                    area_name_dict[employee["area"]],
                    employee["nome"] + " " + employee["sobrenome"],
                    employee["salario"],
                )
            )
            for employee in employee_by_area[key]
            if employee["salario"] == max_salary
        ]
        _ = [
            print(
                "area_min|{}|{}|{}".format(
                    area_name_dict[employee["area"]],
                    employee["nome"] + " " + employee["sobrenome"],
                    employee["salario"],
                )
            )
            for employee in employee_by_area[key]
            if employee["salario"] == min_salary
        ]
        print("area_avg|{}|{:.2f}".format(area_name_dict[key], average_salary))


def calculate_employees_max_min(data):
    """
    Function to calculate the largest and smallest number of employees per area
    """
    area_list = [area_dict["codigo"] for area_dict in data["areas"]]
    employee_by_area = {key: 0 for key in area_list}
    area_name_dict = {
        area_dict["codigo"]: area_dict["nome"] for area_dict in data["areas"]
    }
    for employee in data["funcionarios"]:
        employee_by_area[employee["area"]] += 1
    employees_by_area_dict = {employee_by_area[key]: [] for key in employee_by_area}
    for area in employee_by_area:
        employees_by_area_dict[employee_by_area[area]].append(area_name_dict[area])
    most_employees = max(employees_by_area_dict.keys())
    least_employees = min(employees_by_area_dict.keys())
    for area in employees_by_area_dict[most_employees]:
        print("most_employees|{}|{}".format(area, most_employees))
    for area in employees_by_area_dict[least_employees]:
        print("most_employees|{}|{}".format(area, least_employees))


def last_name_max_salary(data):
    """
    Function to calculate max salary of employees with the same last name
    """
    last_name_count = {employee["sobrenome"]: 0 for employee in data["funcionarios"]}
    for employee in data["funcionarios"]:
        last_name_count[employee["sobrenome"]] += 1
    last_name_count = {
        key: last_name_count[key] for key in last_name_count if last_name_count[key] > 1
    }
    last_name_to_calculate = {key: [] for key in last_name_count}
    for key in last_name_to_calculate:
        last_name_to_calculate[key] = [
            employee
            for employee in data["funcionarios"]
            if key == employee["sobrenome"]
        ]
    last_name_calculate = {key: [] for key in last_name_to_calculate}
    for key in last_name_calculate:
        last_name_calculate[key] = [
            employee["salario"] for employee in last_name_to_calculate[key]
        ]
        max_salary = max(last_name_calculate[key])
        _ = [
            print(
                "last_name_max|{}|{} {}|{}".format(
                    employee["sobrenome"],
                    employee["nome"],
                    employee["sobrenome"],
                    employee["salario"],
                )
            )
            for employee in last_name_to_calculate[key]
            if employee["salario"] == max_salary
        ]


def main():
    """
    Main function to execute all calculations
    """
    this_folder = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(this_folder, "funcionarios-10K.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
        calculate_salary(data)
        calculate_salary_by_area(data)
        calculate_employees_max_min(data)
        last_name_max_salary(data)


if __name__ == "__main__":
    main()
