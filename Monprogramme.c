#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp_read, *fp_write;
    double note;
    int count = 0;

    fp_read = fopen("MesNotes.txt", "r");
    if (!fp_read) {
        perror("Erreur lors de l'ouverture du fichier MesNotes.txt");
        return EXIT_FAILURE;
    }

    fp_write = fopen("FilteredNotes.txt", "w");
    if (!fp_write) {
        perror("Erreur lors de l'ouverture du fichier FilteredNotes.txt");
        fclose(fp_read);
        return EXIT_FAILURE;
    }

    while (fscanf(fp_read, "%lf\n", &note) != EOF) {
        if (count < 512) {
            fprintf(fp_write, "%.2f\n", note);
            count++;
        } else {
            fprintf(stderr, "Erreur: Le nombre de notes dépasse la limite autorisée de 512.\n");
            fclose(fp_read);
            fclose(fp_write);
            return EXIT_FAILURE;
        }
    }

    fclose(fp_read);
    fclose(fp_write);
    system("python3 process_notes.py");  // Lancer le script Python
    return EXIT_SUCCESS;
}

