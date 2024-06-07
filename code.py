# fetch data from oracle database datewise by passig credential of conncetion
def fetch_data_backups(self, credentials, model_id, date):
    connection = cx_Oracle.connect(f'{credentials[0]}/{credentials[1]}@{credentials[2]}')
    cursor = connection.cursor()

    if isinstance(date, str):
        date_str = date
    else:
        raise ValueError("date must be a string in 'YYYY-MM-DD' format")

    cursor.execute(
        """
        SELECT command_template 
        FROM om_config_command_templates_bkp 
        WHERE model_id = :model_id
        AND CREATED_ON >= TO_DATE(:date_str, 'YYYY-MM-DD')
        AND CREATED_ON < TO_DATE(:date_str, 'YYYY-MM-DD') + INTERVAL '1' DAY
        """,
        {'model_id': model_id, 'date_str': date_str}
    )

    result = cursor.fetchone()
    data = result[0].read() if result else None

    cursor.close()
    connection.close()

    return data
  
credentials_demo = ('haider_1234', 'hjkfh$78fhjk', '13.189.999.01:1876/haideeDemo1')
z=fetch_data_backups(credentials_demo, 1219,'2098-12-31')

