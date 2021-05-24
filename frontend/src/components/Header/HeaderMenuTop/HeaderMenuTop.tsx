import React from 'react'
import cn from 'classnames'
import { RouteComponentProps } from 'react-router'
import MenuTopCity from './MenuTopCity'
import MenuTopButtons from './MenuTopButtons'
import styles from './HeaderMenuTop.module.scss'

type PropsType = RouteComponentProps

export const HeaderMenuTop: React.FC<PropsType> = () => {
    const menuTopTel = cn(styles.menuTopTel)

    return (
        <div className={styles.menuTop}>
            <MenuTopCity/>
            <a className={menuTopTel} href="tel:89261113978">
                +7 (926) 111-39-78
            </a>
            <MenuTopButtons/>
        </div>
    )
}