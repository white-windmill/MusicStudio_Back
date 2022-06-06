
se  bounce a message back and forth across the screen
 *    compile  cc hello5.c -lcurses -o hello5
 */
#include <curses.h>
#include <signal.h>
#include <aio.h>
#include <stdio.h>
#include <sys/time.h>

#define	LEFTEDGE	10
#define	RIGHTEDGE	30
#define	ROW		10

int stop=0,sign;//sign是判断小球在暂停前是向左移动还是向右移动，0向左移动，1向右移动
//stop是判断是暂停还是取消暂停 1是暂停，0是取消暂停
int	dir = +1;
int	pos = LEFTEDGE ;
char	message[] = "o";
char	blank[]   = " ";
int 	done=0;

int row = ROW;
int col = LEFTEDGE;

struct	aiocb	kbuf;

set_ticker( n_msecs )
{
        struct itimerval new_timeset;
        long    n_sec, n_usecs;

        n_sec = n_msecs / 1000 ;
        n_usecs = ( n_msecs % 1000 ) * 1000L ;

        new_timeset.it_interval.tv_sec  = n_sec;        /* set reload  */
        new_timeset.it_interval.tv_usec = n_usecs;      /* new ticker value */
        new_timeset.it_value.tv_sec     = n_sec  ;      /* store this   */
        new_timeset.it_value.tv_usec    = n_usecs ;     /* and this     */

        return setitimer(ITIMER_REAL, &new_timeset, NULL);
}


void move_msg()
{
	signal(SIGALRM, move_msg);	/* reset, just in case	*/
	move( row, col );
	addstr( blank );

	col += dir;			/* move to new column	*/
	move( row, col );		/* then set cursor	*/
	addstr( message );		/* redo message		*/
	move(LINES-1, COLS-1);
	refresh();			/* and show it		*/

	/*
	 * now handle borders
	 */
	pos += dir;
	if ( pos >= RIGHTEDGE ){		/* check for bounce	*/
		dir = -1;
		sign = 0;
		//向左移动,sign=0
	}
	if ( pos <= LEFTEDGE ){
		dir = +1;
		sign = 1;
		//向右移动,sign=1
    }
}

void setup_aio(){
	static char input[1];
	
	kbuf.aio_fildes = 0;
	kbuf.aio_buf = input;  //input buffer;
	kbuf.aio_nbytes = 1;
	kbuf.aio_offset = 0;
	
	kbuf.aio_sigevent.sigev_notify = SIGEV_SIGNAL;
	kbuf.aio_sigevent.sigev_signo = SIGIO;
}

void oninput(){
	int c;
	char* cp = (char*)kbuf.aio_buf;

	if(aio_error(&kbuf) != 0)
		perror("reading failed\n");
	
	else if(aio_return(&kbuf) == 1){
		c = *cp;
		if( c == 'q'){
			done=1;
			printf("doen=1\n");		
		}else if ( c == 'w'){//向上移动
			move(row, col);
			addstr(blank);//否则屏幕会残留小球痕迹
			if (row > 0)//防止越界
			{
				row -= 1;
			}else{
				row = 0;
			}
		}
		else if ( c == 's'){//向下移动
			move(row, col);
			addstr(blank);//否则屏幕会残留小球痕迹
			if (row < LINES - 1){//防止越界
				row += 1;
			}else{
				row = 0;
			}
		}
		else if( c == 'c'){
			stop = !stop;
			if(stop) {//小球停止移动
			    dir = 0;
			}
			else{
			    if(sign){//恢复暂停前状态
                    dir = +1;
                }else{
				    dir = -1;
                }
			}
		}
	}
	aio_read(&kbuf);
}

int main()
{
	char c;
	int delay=200;
	
	initscr();
	clear();

	move(ROW, pos);
	addstr(message);
	move(LINES-1,COLS-1);

	signal(SIGIO, oninput);
	setup_aio();
	aio_read(&kbuf);

	signal(SIGALRM, move_msg);
	set_ticker(delay);

	while(!done){
		pause();
	}

	endwin();
	return 0;
}

