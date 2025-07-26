#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// new data structure
typedef struct
{
    char *name;
    char *number;
} PERSON;

// Global variables
int size = 0;
PERSON *phonebook = NULL;


// Function prototypes
char *search(string name);
void add(char *name, char *number);
int delete(char *name, char *number);


int main(void)
{
    while(true)
    {
            // Ask user for mode
        char *mode = get_string("Mode (Search, Add, Delete, Exit): ");

        // search
        if (strcmp(mode, "Search") == 0)
        {
            char *z = "y";
            while (strcmp(z, "y") == 0)
            {
                char *name = get_string("Name: ");
                char *result = search(name);
                if (strlen(result) > 1)
                {
                    printf("Number: %s\n", result);

                }
                if (strcmp(result, "0") == 0)
                {
                    printf("Phonebook empty.\n");

                }
                else if (strcmp(result, "1") == 0)
                {
                    printf("Not found.\n");
                }
                z = get_string("Keep going? y or n: ");
            }


        }

        // add
        else if (strcmp(mode, "Add") == 0)
        {
            char *x = "y";
            while (strcmp(x, "y") == 0)
            {
                char *name = get_string("Name: ");
                char *number = get_string("Number: ");
                add(name, number);
                printf("Added.\n");
                size += 1;
                x = get_string("Keep going? y or n: ");
            }

        }


        // delete
        else if (strcmp(mode, "Delete") == 0)
        {
            char *y = "y";
            while (strcmp(y, "y") == 0)
            {
                char *name = get_string("Name: ");
                char *number = get_string("Number: ");
                int result = delete(name, number);
                if (result == 1)
                {
                    printf("Empty phonebook.\n");

                }
                else if (result == 2)
                {
                    printf("Not found.\n");
                }
                else
                {
                    printf("Deleted.\n");
                    size -= 1;
                }

                y = get_string("Keep going? y or n: ");
            }


        }

        // exit

        else if (strcmp(mode, "Exit") == 0)
        {
            printf("Exited.\n");
            break;
        }

        else
        {
            printf("Invalid mode.\n");
        }


    }


}


char *search(char *name)
{
    if (size == 0)
    {
        return "0";
    }
    for (int i = 0; i < size; i++)
    {
        if (strcmp(phonebook[i].name, name) == 0)
        {
            return phonebook[i].number;
        }
    }
    return "1";


}

void add(char *name, char *number)
{
    phonebook = realloc(phonebook, (size + 1) * sizeof(PERSON));
    if (phonebook == NULL)
    {
        printf("Memory allocation failed.\n");
        return;
    }
    phonebook[size].name = name;
    phonebook[size].number = number;
}


int delete(char *name, char *number)
{

    if (size == 0)
    {
        return 1;
    }

    for (int i = 0; i < size; i++)
    {
        if (strcmp(phonebook[i].name, name) == 0 && strcmp(phonebook[i].number, number) == 0)
        {


            for (int j = i; j < size - 1; j++)
            {
                phonebook[j] = phonebook[j + 1];
            }

            phonebook = realloc(phonebook, (size - 1) * sizeof(PERSON));
            return 0;
        }




    }
    return 2;
}
