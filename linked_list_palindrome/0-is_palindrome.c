#include "lists.h"

/**
* is_palindrome- func
* @head: listint_t **
* Return: int
*/
int is_palindrome(listint_t **head)
{
	listint_t **ph;

	ph = &(*head);
	return (ch(*head, ph));
}

/**
* ch- func
* @fe: listint_t *
* @ph: listint_t **
* Return: int
*/
int ch(listint_t *fe, listint_t **ph)
{
	int rv;
	listint_t *aux;

	if (fe)
		rv = ch(fe->next, ph);
	else
		return (1);
	aux = *ph;
	*ph = aux->next;
	if (fe->n == aux->n)
		return (1 * rv);
	else
		return (0);
}