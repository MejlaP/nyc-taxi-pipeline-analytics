from datetime import date
from dateutil.relativedelta import relativedelta

def get_target_yyyymm(month_ago=6):
    """
    Returns the year-month string (yyyy-MM) for the given number of months ago.
    """
    target_date = date.today() - relativedelta(months=month_ago)
    return target_date.strftime("%Y-%m")

def get_month_start_n_months_ago(month_ago: int = 6) -> date:
    """
    Returns the date representing the first day of the month, 'n' months ago.

    Parameters:
        month_ago (int): The number of months to go back from today. Default is 6 months.

    Returns:
        date: A date object set to the first day of the target month.
        """
    return (date.today().replace(day=1) - relativedelta(months=month_ago))
