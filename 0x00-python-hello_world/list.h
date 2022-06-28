#include "lists.h"

/**
 * check_cycle - check if list is cycle
 * @list: type listint_t
 * Return: always int
 * case: 1 true, 0 false
 */

int check_cycle(listint_t *list)
{
listint_t *past = list, *futur = list;

while (past != NULL && futur != NULL && futur->next != NULL)
{
past = past->next;
futur = futur->next->next;
if (past == futur)
return (1);
}
return (0);
}
