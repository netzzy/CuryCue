# conn=mysql.connector.connect(host='localhost',database='cosmos',user='root',password='')
# if conn.is_connected():
#     print('Connected to MySQL database')
# self.conn=conn        


# cursor = self.conn.cursor()
# cursor.execute("SELECT ls.id, `Launch_id`,`Site_id`,`Tle_id`, ls.`Name`, `Name_2`, `Name_3`, `Suc`, `Satellite_Number`, `LaunchYear2d`, `Launch_number_of_year`, `Piece_of_the_launch`, `LV`, `Site_name`, `Site_location`, sites.UName, `Site_long`, `Site_lat`, `tle1`, `tle2`, x,y,z FROM launches_sites_tles as ls, sites WHERE sites.id=ls.Site_id ")
# rows = cursor.fetchall()

# satDataHeader=['id', 'Launch_id','Site_id','Tle_id', 'Name', 'Name_2', 'Name_3', 'Suc', 'Satellite_Number', 'LaunchYear2d', 'Launch_number_of_year', 'Piece_of_the_launch', 'LV', 'Site_name', 'Site_location', 'Site_uname', 'Site_long', 'Site_lat', 'tle1', 'tle2','x','y','z']


# print('Total Row(s):', cursor.rowcount)
# nn=0
# for row in rows:
# 	self.satDbInfo[int(row[0] )]=row
# 	nn+=1

# cursor = self.conn.cursor()
# cursor.execute("DELETE FROM td_launch_control")
# cursor.execute("UPDATE launches_sites_tles SET launched=0")
# cursor.execute("UPDATE `td_sat_workers` SET `id_launched` = NULL")
# self.conn.commit()



# cursor = self.conn.cursor()
# cursor.execute("DELETE FROM td_launch_control")
# cursor.execute("UPDATE launches_sites_tles SET launched=0")
# cursor.execute("UPDATE `td_sat_workers` SET `id_launched` = NULL")
# self.conn.commit()        



# cursor = self.conn.cursor()
# cursor.execute("DELETE FROM td_launch_control")
# cursor.execute("UPDATE launches_sites_tles SET launched=0")
# cursor.execute("UPDATE `td_sat_workers` SET `id_launched` = NULL")
# self.conn.commit()        



# cursor = self.conn.cursor()
# cursor.execute("DELETE FROM td_launch_control")
# cursor.execute("UPDATE launches_sites_tles SET launched=0")
# cursor.execute("UPDATE `td_sat_workers` SET `id_launched` = NULL")
# self.conn.commit()        

# cursor.execute("SELECT w.id, c.id_lst FROM td_sat_workers as w, td_launch_control  as c WHERE w.id=c.id_sat_worker ORDER BY w.id")
# rows=cursor.fetchall()
# self.currentSatsInSpace=cursor.rowcount
# me.parent().par.Activesats=self.currentSatsInSpace
# if cursor.rowcount>0:
# 	for r in rows:
# 		op("WORKERS_ID")[int(r[0]), 0]=r[1]



# cursor = self.conn.cursor()
# cursor.execute("SELECT id, `Launch_id`,`Site_id`,`Tle_id`, `Name`, `Name_2`, `Name_3`, `Suc`, `Satellite_Number`, `LaunchYear2d`, `Launch_number_of_year`, `Piece_of_the_launch`, `LV`, `Site_name`, `Site_location`, `Site_uname`, `Site_long`, `Site_lat`, `tle1`, `tle2`, x,y,z FROM launches_sites_tles WHERE id = '"+str(int(myid))+"'")
# rows = cursor.fetchall()        