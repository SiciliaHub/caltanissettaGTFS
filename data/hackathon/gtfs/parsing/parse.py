import csv
import datetime

out_dir = "/home/davide/Scrivania/SOD17/"
in_dir = "/home/davide/Scrivania/SOD17/"

# lo stop_id è l'identificativo della fermata, c'è un file unico di input che contiene l'indirizzo
# che ci farà da chiave stops.txt in formato standard: https://developers.google.com/transit/gtfs/reference/stops-file
stops_dict = {}
with open(in_dir + "stops.txt", 'r') as stops_file:
    is_header = True
    csv_reader = csv.reader(stops_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        if not is_header:
            # controllo che non ci sia già la key perché potrebbe essere ripetuta su linee diverse
            # stop_id,stop_name,stop_lat,stop_lon
            stop_id = row[0]
            stop_name = row[1]
            stop_lat = row[2].replace(",", ".")
            stop_lon = row[3].replace(",", ".")
            if not stop_name in stops_dict.keys():
                stops_dict[stop_name] = {
                    "stop_id": stop_id,
                    "stop_lat": stop_lat,
                    "stop_lon": stop_lon
                }
        is_header = False

# service_id è una costante unica per tutta la scat
service_id = "buscl"

# https://developers.google.com/transit/gtfs/reference/routes-file
routes_file = open(out_dir + "routes.txt", 'w')
routes_file_writer = csv.writer(routes_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# required: route_id, route_short_name, route_long_name, route_type (3=Bus),
routes_file_writer.writerow(['route_id', 'route_short_name', 'route_long_name', 'route_type'])

# https://developers.google.com/transit/gtfs/reference/trips-file
# gli altri sono opzionali; dal momento che a CL le linee sono prevalentemente circolari qui non ho
# necessità di alcun campo opzionale
trips_file = open(out_dir + "trips.txt", 'w')
trips_file_writer = csv.writer(trips_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# required: route_id, service_id (da calendar.txt), trip_id
trips_file_writer.writerow(['route_id', 'service_id', 'trip_id'])

# stops.txt è l'anagrafica geolocalizzata delle fermate e lo ricevo in input
# stop_times.txt
stop_times_file = open(out_dir + "stop_times.txt", 'w')
stop_times_file_writer = csv.writer(stop_times_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# required trip_id, arrival_time, departure_time, stop_id (da stops.txt), stop_sequence
stop_times_file_writer.writerow(['trip_id', 'arrival_time', 'departure_time', 'stop_id', 'stop_sequence'])

linee = []
linea2 = {
    "path_file": in_dir + "2.csv",
    "orario_inizio": datetime.datetime(2000, 1, 1, 7, 20),
    "orario_fine": datetime.datetime(2000, 1, 1, 20, 00),
    "frequenza": datetime.timedelta(minutes=40)
}
# linee.append(linea2)
linea3 = {
    "path_file": in_dir + "3.csv",
    "orario_inizio": datetime.datetime(2000, 1, 1, 7, 45),
    "orario_fine": datetime.datetime(2000, 1, 1, 19, 45),
    "frequenza": datetime.timedelta(minutes=60)
}
linee.append(linea3)

'''
L'header del file contiene alla terza posizione una descrizione "LINEA 3 - ZIR - SAN LUCA - FREQUENZA 60'"
Nelle note orario inizio, fine e frequenza

CAMPI IN INGRESSO
N.RO, ORARIO  PASSAGGIO FERMATA, INDIRIZZO FERMATA, IMPIANTO, NOTE

'''

id_route = 1
for linea in linee:
    out_file_path = linea["path_file"].replace('.csv', '_out.csv')
    out_file = open(out_file_path, 'w')
    out_writer = csv.writer(out_file, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # trip_id è univoco anche tra corse diverse
    trip_id = 1
    route_id = 1
    with open(linea["path_file"], 'r') as in_file:
        # per ogni linea una entry in routes.txt
        csv_reader = csv.reader(in_file, delimiter='\t', quotechar='|')
        h = csv_reader.__next__()
        routes_file_writer.writerow([str(id_route), h[2], h[2], '3'])

        orario_corrente = linea["orario_inizio"]
        '''
        In output aggiungere un id numerico della corsa
        '''
        is_header = True
        while orario_corrente <= linea["orario_fine"]:
            stop_sequence = 1
            trips_file_writer.writerow([str(route_id), service_id, str(trip_id)])
            for row in csv_reader:
                if not is_header:
                    ore = int(row[1].split(".")[0])
                    minuti = int(row[1].split(".")[1])
                    orario = datetime.datetime(2000,1,1,ore, minuti) + ((trip_id - 1) * linea["frequenza"])
                    ore_minuti = ("%s:%s:00" % (orario.hour, orario.minute))
                    if not row[2] in stops_dict.keys():
                        raise Exception("%s mancante nel file stops.txt" % row[2])
                    # lookup dal file stops.txt passando da un dict
                    stop_id = stops_dict[row[2]]["stop_id"]
                    stop_times_file_writer.writerow(
                        [str(trip_id), ore_minuti, ore_minuti, str(stop_id), str(stop_sequence)])
                    out_writer.writerow([route_id, row[0], ore_minuti, row[2], row[3]])
                    stop_sequence += 1
                is_header = False
            orario_corrente = orario_corrente + linea["frequenza"]
            # mi riposiziono all'inizio del file
            in_file.seek(0)
            is_header = True
            csv_reader = csv.reader(in_file, delimiter='\t', quotechar='|')
            trip_id += 1 #############################
        route_id += 1 ############################
out_file.close()
routes_file.close()
trips_file.close()
stop_times_file.close()