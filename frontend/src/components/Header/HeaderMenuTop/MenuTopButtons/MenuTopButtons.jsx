import React from 'react'
import styles from './MenuTopButtons.module.scss'
import IconBasket from '../../../UI/icons/iconBasket'

const MenuTopButtons = () => {
    return (
        <ul className={styles.menuTopButtons}>
            <li>
                <IconBasket/>
            </li>
        </ul>
    )
}

export default MenuTopButtons