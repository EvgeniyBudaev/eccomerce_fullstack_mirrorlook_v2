import React from 'react'
import Classnames from 'classnames'
import EmptyBlockToHomePage from "./Empty"
import Logo from "./Logo"
import HeaderMenuBottom from "./HeaderMenuBottom"
import HeaderCategories from "./HeaderCategories"
import HeaderMenuTop from "./HeaderMenuTop"
import styles from './Header.module.scss'

export const Header = () => {
    const headerStyles = Classnames(
        styles.header,
    )

    return (
        <>
            <div className={headerStyles}>
                <div className={styles.container}>
                    <div className={styles.innerMenuAndLogo}>
                        <div className={styles.logoAndHamburger}>
                            <Logo />
                        </div>
                        <div className={styles.menu} data-headermenu="">
                            <HeaderMenuTop />
                            <HeaderMenuBottom />
                        </div>
                    </div>
                    <HeaderCategories />
                </div>
            </div>
            <EmptyBlockToHomePage />
        </>
    )
}