##
#Script pour la creation des tables en base de données
##
from config import *
import psycopg2

params = config()

myConnection = psycopg2.connect(**params)

cur = myConnection.cursor()

cur.execute("create table if not exists ipasn_asn ( id SERIAL PRIMARY KEY, asn int, created_at date);")

cur.execute("create table if not exists ipasn_ipv4 ( id SERIAL PRIMARY KEY, bloc_ipv4 int, allocated int, assigned int, created_at date);")

cur.execute("create table if not exists ipasn_ipv6 ( id SERIAL PRIMARY KEY , bloc_ipv6 int, allocated int, assigned int, created_at date);")

cur.execute("create table if not exists api_ipasn_asn ( id SERIAL PRIMARY KEY , num_asn int, owner_asn varchar(225), status_asn varchar(225), afrinic_created_at int, created_at date);")

cur.execute("create table if not exists api_ipasn_ipv4 ( id SERIAL PRIMARY KEY , bloc_ip varchar(225), cidr_ip int, status_ip varchar(225), afrinic_created_at int, asn_ip varchar(225), created_at date);")

cur.execute("create table if not exists api_ipasn_ipv6 ( id SERIAL PRIMARY KEY , bloc_ip varchar(225), cidr_ip int, status_ip varchar(225), afrinic_created_at int, asn_ip varchar(225), created_at date);")

cur.execute("create table if not exists ipasn ( id SERIAL PRIMARY KEY , ipaddr varchar(25), cidr varchar(25), ip_date varchar(25), ip_status varchar(25), asn_num varchar(25), asn_date varchar(25), asn_status varchar(25), Owner varchar(225), created_at date);")

#Create database domain bj
cur.execute("create table if not exists domain ( id SERIAL PRIMARY KEY, total_domain int, actifs_domain int, expired_domain int, year int, created_at date);")

#Create database sonde bj
cur.execute("create table if not exists sonde ( id SERIAL PRIMARY KEY , total int, abandonned int, connected int, disconnected int, never_connected int, created_at date);")

#Create database penetration bj
cur.execute("create table if not exists penetration ( id SERIAL PRIMARY KEY , internet_fixe float(2), internet_mobile float(2), year int, created_at date);")

#Create database teledensite bj
cur.execute("create table if not exists teledensite ( id SERIAL PRIMARY KEY , teledensite float(2), year int, created_at date);")

#Create database repartition_debit bj
cur.execute("create table if not exists repartition_debit ( id SERIAL PRIMARY KEY , debit varchar(255), repartition float(2), year int,created_at date);")

#Create database repartision_technologie bj
cur.execute("create table if not exists repartition_technologie ( id SERIAL PRIMARY KEY , technologie varchar(225), repartition float(2), year int, created_at date);")

#Create database evolution_fai bj
cur.execute("create table if not exists evolution_fai ( id SERIAL PRIMARY KEY , operateur varchar(225), evolution int, year int, created_at date);")

#Create database evolution_fixe bj
cur.execute("create table if not exists evolution_fixe ( id SERIAL PRIMARY KEY , technologie varchar(255), evolution int, year int, created_at date);")

#Create database parc_abonnes bj
cur.execute("create table if not exists parc_abonnes ( id SERIAL PRIMARY KEY , operateur varchar(255), abonnes int, year int, augmentation int, nbre_jour float(), nbre_heure float(), nbre_minute float(),  created_at date);")

myConnection.commit()
print('Creation ok')
myConnection.close()
